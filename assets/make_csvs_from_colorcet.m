% make_csvs_from_colorcet.m
% 1. Requires latest colorcet.m from peterkovesi.com in same directory
% 2. Set the name of the dir for the new colormaps
% 3. Update mapnames cell array below from colorcet.m
% 4. After running this in octave or MATLAB, follow instructions in CET_merge.py

new_mapsdir = 'CETperceptual_csv_0_1_v3';

% copied from colorcet.m
mapnames = {
{ 'L1'  'L01'  'GREY'  'GRAY' }
{ 'L2'  'L02'  'REDUCEDGREY' }
{ 'L3'  'L03'  'KRYW'  'HEAT'  'FIRE' }
{ 'L4'  'L04'  'KRY'  'YELLOWHEAT' }
{ 'L5'  'L05'  'KGY' }
{ 'L6'  'L06'  'KBC' }
{ 'L7'  'L07'  'BMW' }
{ 'L8'  'L08'  'BMY' }
{ 'L9'  'L09'  'BGYW' }
{ 'L10'  'GEOGRAPHIC' }
{ 'L11'  'GEOGRAPHIC2' }
{ 'L12'  'DEPTH' }
{ 'L13'  'REDTERNARY' }
{ 'L14'  'GREENTERNARY' }
{ 'L15'  'BLUETERNARY' }
{ 'L16'  'KBGYW' }
{ 'L17'  'WORB' }
{ 'L18'  'WYOR' }
{ 'L19'  'WCMR' }
{ 'L20'  'GOULDIAN' }
{ 'D1'  'D01'  'BWR'  'COOLWARM' }
{ 'D1A'  'D01A'  'BWRA' }
{ 'D2'  'D02'  'GWV' }
{ 'D3'  'D03'  'GWR' }
{ 'D4'  'D04'  'BKR' }
{ 'D5'  'D05'  'GKR' }
{ 'D6'  'D06'  'BKY' }
{ 'D7'  'D07'  'BJY'  'DIVBJY' }
{ 'D8'  'D08'  'BJR' }
{ 'D9'  'D09' }
{ 'D10' }
{ 'D11' }
{ 'D12' }
{ 'D13'  'BWG' }
{ 'C1'  'C01' }
{ 'C2'  'C02'  'PHASE4' }
{ 'C3'  'C03' }
{ 'C4'  'C04'  'PHASE2' }
{ 'C5'  'C05'  'CYCLICGREY' }
{ 'C6'  'C06' }
{ 'C7'  'C07' }
{ 'C8'  'C08' }
{ 'C9'  'C09' }
{ 'C10' }
{ 'C11' }
{ 'R1'  'R01'  'RAINBOW' }
{ 'R2'  'R02'  'RAINBOW2' }
{ 'R3'  'R03'  'RAINBOW3' }
{ 'R4'  'R04'  'RAINBOW4' }
{ 'I1'  'I01' }
{ 'I2'  'I02' }
{ 'I3'  'I03' }
{ 'CBL1' }
{ 'CBL2' }
{ 'CBL3' }
{ 'CBL4' }
{ 'CBD1' }
{ 'CBD2' }
{ 'CBC1' }
{ 'CBC2' }
{ 'CBTL1' }
{ 'CBTL2' }
{ 'CBTL3' }
{ 'CBTL4' }
{ 'CBTD1' }
{ 'CBTC1' }
{ 'CBTC2' }
};

aliases = containers.Map();
mapping = containers.Map();

existing_csvs = arrayfun(@(f) f.name, dir('**/*.csv'), 'UniformOutput', false);

for mni = 1:numel(mapnames)
    % first string is the CET- name. The rest are some of the aliases
    mapname = mapnames{mni}{1};
    othernames = mapnames{mni}(2:end);
    % don't keep names like D04
    othernames = othernames(cellfun(@isempty, regexp(othernames, '^[A-Z][0-9]+')));
    for ni = [1, 2]  % second time is s25
        if ni == 2 && isempty(regexp(mapname, '^C\d+')), break, end  % only do s25 for cyclic
        mapfname = sprintf('CET-%s', mapname);
        if ni == 2
            mapfname = [mapfname, 's'];
        end
        switch ni
            case 1
                [map, descriptorname, description] = colorcet(mapname);
            case 2
                [map, descriptorname, description] = colorcet(mapname, 'shift', 0.25);
        end
        dnames = strsplit(descriptorname, ' ');  % Some descriptorname entries have multiple verions
        descriptorname = strrep(dnames{end}, '_n256', '');
        if ni == 2
            descriptorname = [descriptorname, '_s25'];
        end
        othernames = [othernames, dnames(1:end-1)];
        if ~isempty(othernames) && ni == 1
            aliases(descriptorname) = othernames;
        end
        mapping(mapfname) = descriptorname;
        % If the map doesn't exist, write it.
        mapcsvname = [mapfname, '.csv'];
        if ismember(mapcsvname, existing_csvs), continue, end
        if ~exist(new_mapsdir, 'dir')
            mkdir(new_mapsdir);
        end
        csvwrite(fullfile(new_mapsdir, mapcsvname), map, 'precision', '%0.5g');
    end
end

% Create CET_updates.py to use in CET_merge.py
fupdates = fopen('CET_updates.py', 'w');
fprintf(fupdates, 'new_aliases = dict(\n');
keys = aliases.keys();
for keyi = 1:numel(keys)
    key = keys{keyi};
    als = strrep(aliases(key), '-', '_');  % can't have hyphens in aliases
    if numel(als) == 0, continue, end
    fprintf(fupdates, '    %s = [', strrep(key, '-', '_'));
    for ali = 1:numel(als)
        fprintf(fupdates, '''%s'',', lower(als{ali}));
    end
    fprintf(fupdates, '],\n');
end
fprintf(fupdates, ')\n');
fprintf(fupdates, '\n');

fprintf(fupdates, 'new_mapping = {\n')
keys = mapping.keys();
for keyi = 1:numel(keys)
    key = keys{keyi};
    fprintf(fupdates, '    ''%s'': ''%s'',\n', key, mapping(key));
end
fprintf(fupdates, '}\n');
fprintf(fupdates, '\n');

fprintf(fupdates, 'new_mapsdir = "%s"\n', new_mapsdir);

fclose(fupdates);

