#include<string.h>
#include<omnetpp.h>

using namespace omnetpp;
class Txc: public cSimpleModule
{
    protected:
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
};

Define_Module(Txc);

void Txc::initialize()
{
//    if (strcmp("tower1", getName())==0)
//    {
//        cMessage *msg=new cMessage("PING");
//        send(msg, "out");
//    }

}
void Txc::handleMessage(cMessage *msg)
{
    send (msg, "out");
}
