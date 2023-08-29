#include<string.h>
#include<omnetpp.h>

using namespace omnetpp;
class Txc1: public cSimpleModule
{
    protected:
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
};

Define_Module(Txc1);

void Txc1::initialize()
{
    cMessage *msg=new cMessage("PING");
    cMessage *msg2=new cMessage("PING");
    cMessage *msg3=new cMessage("PING");
    cMessage *msg4=new cMessage("PING");
    cMessage *msg5=new cMessage("PING");

    send(msg, "out1");
    send(msg2, "out2");
    send(msg3, "out3");
    send(msg4, "out4");
    send(msg5, "out5");
}
void Txc1::handleMessage(cMessage *msg)
{
//    send (msg, "out");
}
