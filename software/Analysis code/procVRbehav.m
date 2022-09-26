function [vrBehStruc] = procVRbehav()

[filename, path] = uigetfile('*.txt', 'Select VR .txt data file');

[fullCell] = textread([path '/' filename], '%s', 'delimiter', '\n');


pos=[]; posTime=[];
vel=[]; 
lickTime=[]; lickPos=[];
rewTime=[]; rewPos=[];
lapNum = 1; lapTime=[];

%% Read in the events
tic;
for i=1:length(fullCell) % for each event in text file
    try
        ev = fullCell{i}; % extract event string
        evTime = str2double(ev(strfind(ev,'ms')+3:end));
        if contains(ev,'lap')
            evTime = str2double(ev(strfind(ev,'ms')+3:end)); % +8 for 'millis'
            lapNum=lapNum+1;
            lapTime = [lapTime evTime];
        elseif contains(ev, 'currPos')
            currPos = str2double(ev(strfind(ev,'currPos')+8:strfind(ev,'ms')-3));
            currVel = str2double(ev(strfind(ev,'vel')+4:strfind(ev,'currPos')-3));
            pos = [pos currPos];
            vel = [vel currVel];
            posTime = [posTime evTime];
        elseif contains(ev, 'lick')
            lickTime = [lickTime evTime];
            lickPos = [lickPos currPos];
        elseif contains(ev, 'REWARD')
            rewTime = [rewTime evTime];
            rewPos = [rewPos currPos];
        end
    catch
    end
end
toc;


vrBehStruc.filename = filename;
vrBehStruc.lapTime=lapTime;
vrBehStruc.pos=pos;
vrBehStruc.posTime=posTime;
vrBehStruc.vel=vel;
vrBehStruc.lickTime=lickTime;
vrBehStruc.lickPos=lickPos;
vrBehStruc.rewTime=rewTime;
vrBehStruc.rewPos=rewPos;

% Plot
nbins = 40;
maxPos = max(pos); %(~isNaN(pos)));
edges = 0:round(maxPos/nbins):maxPos;

figure;
subplot(2,1,1);
histogram(lickPos, edges); title(filename); xlabel('position'); ylabel('licks');
subplot(2,1,2);
histogram(rewPos, edges); title(filename); xlabel('position'); ylabel('rews');

[N, edges, bin] = histcounts(pos, edges);
for j=1:length(N)
    velHist(j) = sum(vel(find(bin==j)))/length(vel(find(bin==j)));
end
figure; bar(velHist); title(filename); xlabel('position'); ylabel('vel');

[lickByLap] = vrLickByLap(vrBehStruc);
vrBehStruc.lickByLap = lickByLap;
