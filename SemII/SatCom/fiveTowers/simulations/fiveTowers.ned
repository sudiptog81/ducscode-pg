package fivetowers.simulations;

simple Txc
{
    gates:
        input in;
        output out;
}

simple Txc1
{
    gates:
        input in1;
        input in2;
        input in3;
        input in4;
        input in5;
        output out1;
        output out2;
        output out3;
        output out4;
        output out5;
}

network fiveTowers
{
    @display("bgb=529,346");
    submodules:
        tower1: Txc {
            @display("p=36,186");
        }
        tower2: Txc {
            @display("p=231,76");
        }
        tower4: Txc {
            @display("p=363,272");
        }
        tower5: Txc {
            @display("p=131,272");
        }
        tower3: Txc {
            @display("p=458,170");
        }
        mo: Txc1;
    connections:
        tower1.in <-- {  delay = 100ms; } <-- mo.out1;
        tower1.out --> mo.in1;
        tower2.in <-- {  delay = 100ms; } <-- mo.out2;
        tower2.out --> mo.in2;
        tower3.in <-- {  delay = 100ms; } <-- mo.out3;
        tower3.out --> mo.in3;
        tower5.in <-- {  delay = 100ms; } <-- mo.out4;
        tower5.out --> mo.in5;
        tower4.in <-- {  delay = 100ms; } <-- mo.out5;
        tower4.out --> mo.in4;
}
