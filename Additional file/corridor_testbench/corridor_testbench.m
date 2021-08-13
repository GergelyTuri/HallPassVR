function testbench = corridor_testbench(x)
    out_file = fopen('/Desktop/Corridor_file.txt','w');
    if out_file
        disp('not here');
    end    
    testbench = randi([0,x],1,10);
    %nbytes = fprintf(out_file,'%5d %5d %5d %5d\n',testbench)
    fclose(out_file);
    
end