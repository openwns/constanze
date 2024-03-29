/*******************************************************************************
 * This file is part of openWNS (open Wireless Network Simulator)
 * _____________________________________________________________________________
 *
 * Copyright (C) 2004-2007
 * Chair of Communication Networks (ComNets)
 * Kopernikusstr. 16, D-52074 Aachen, Germany
 * phone: ++49-241-80-27910,
 * fax: ++49-241-80-22242
 * email: info@openwns.org
 * www: http://www.openwns.org
 * _____________________________________________________________________________
 *
 * openWNS is free software; you can redistribute it and/or modify it under the
 * terms of the GNU Lesser General Public License version 2 as published by the
 * Free Software Foundation;
 *
 * openWNS is distributed in the hope that it will be useful, but WITHOUT ANY
 * WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
 * A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 ******************************************************************************/

#ifndef CONSTANZEPDU_HPP
#define CONSTANZEPDU_HPP

#include <WNS/SmartPtr.hpp>

#include <WNS/osi/PDU.hpp>
#include <WNS/osi/PCI.hpp>

#include <WNS/simulator/Time.hpp>


namespace constanze
{
	    //class ConstanzePCI;

	    /**
		 * @brief Simple Packet generated by Constanze processes
         * @author Rainer Schoenen (rs@comnets.rwth-aachen.de)
		 */
        class ConstanzePDU : public wns::osi::PDU
        {
        public:
                ConstanzePDU(Bit _length = 0);
                ~ConstanzePDU();

			    virtual void setLengthInBits(Bit _length);
			    virtual void setTimeStamp(simTimeType time);
			    virtual simTimeType getTimeStamp();

			    //ConstanzePCI* getConstanzePCI() const;

                static ConstanzePDU* castPDU2ConstanzePDU(wns::osi::PDU*);
                static wns::osi::PDU* castConstanzePDU2PDU(ConstanzePDU*);
			    ConstanzePDU* clone()
				{
					return new ConstanzePDU(*this);
				}
#ifndef NDEBUG
		  	    virtual size_t calcObjSize() const
			    {
			 	    return sizeof(*this);
			    }
#endif
		private:
			    virtual Bit doGetLengthInBits() const;
			    Bit length;
			   /**
				* @brief used for delay calculations
				*/
			    simTimeType creationTime;
        };

	    typedef wns::SmartPtr<ConstanzePDU> ConstanzePDUPtr;

}

#endif // CONSTANZEPDU_HPP
