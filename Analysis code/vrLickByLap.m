function vrLickByLap(vrBehStruc)


filename = vrBehStruc.filename;
lapTime=vrBehStruc.lapTime;
pos=vrBehStruc.pos;
posTime=vrBehStruc.posTime;
lickTime=vrBehStruc.lickTime;
lickPos=vrBehStruc.lickPos;
rewTime=vrBehStruc.rewTime;
rewPos=vrBehStruc.rewPos;

nbins = 40;

maxPos = max(pos); %(~isNaN(pos)));
edges = 0:round(maxPos/nbins):maxPos;

lickByLap = zeros(length(lapTime)+1,nbins-1);

for i=0:length(lapTime)
    if i==0
        lickInd = find(lickTime<lapTime(1));
        lickPosLap = lickPos(lickInd);
%         lickHist = histcounts(lickPosLap,nbins);
%         lickByLap(i,:)=lickHist;
    elseif i==length(lapTime)
        lickInd = find(lickTime>lapTime(end));
        lickPosLap = lickPos(lickInd);
    else
        lickInd = find(lickTime>lapTime(i) & lickTime<lapTime(i+1));
        lickPosLap = lickPos(lickInd);
        
    end
    
    lickHist = histcounts(lickPosLap,edges);
    lickByLap(i+1,:)=lickHist;
end

figure; imagesc(lickByLap);colormap('jet'); title(filename);




