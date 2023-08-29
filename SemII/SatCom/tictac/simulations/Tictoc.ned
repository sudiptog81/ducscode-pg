package tictac.simulations;

import tictac.Txc;

network Tictoc
{
    submodules:
        tic: Txc {
            @display("i=device/cellphone");
        }
        toc: Txc {
            @display("i=abstract/router");
        }
        abc: Txc {
            @display("i=device/pc");
        }
    connections:
        tic.out --> {  delay = 100ms; } --> toc.in;
        abc.in <-- {  delay = 100ms; } <-- toc.out;
        abc.out --> {  delay = 100ms; } --> tic.in;
}
