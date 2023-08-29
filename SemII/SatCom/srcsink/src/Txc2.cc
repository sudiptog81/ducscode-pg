//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

#include "Txc2.h"

namespace srcsink {

Define_Module(Txc2);

void Txc2::initialize()
{
    if (par("sendInitialMessage").boolValue())
    {
        cMessage *msg = new cMessage("PING");
        send(msg, "out");
    }
}

void Txc2::handleMessage(cMessage *msg)
{
    // just send back the message we received
    send(msg, "out");
}

}; // namespace
