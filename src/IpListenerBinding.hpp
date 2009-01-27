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

#ifndef CONSTANZE_IPLISTENERBINDING_HPP
#define CONSTANZE_IPLISTENERBINDING_HPP

#include <CONSTANZE/Binding.hpp>
#include <CONSTANZE/Listener.hpp>
#include <CONSTANZE/Generator.hpp>

#include <WNS/service/nl/Service.hpp>
#include <WNS/service/nl/DataHandler.hpp>
#include <WNS/node/component/Component.hpp>
#include <WNS/logger/Logger.hpp>

namespace constanze
{
	class IpListenerBinding:
		public Binding,
		public wns::service::nl::DataHandler
    {
	public:
		IpListenerBinding(const wns::pyconfig::View& _pyco);

		virtual ~IpListenerBinding() {};

		// from Binding
		virtual void
		registerComponent(wns::node::component::Component* _component);

		virtual void
 		sendData(const wns::osi::PDUPtr& _data);

		virtual void
		initBinding(constanze::StartTrigger* trigger);

		virtual void
		releaseBinding(constanze::StopTrigger* trigger);

		void
		registerListener(constanze::Listener* _listener);

		// from DataHandler
		virtual void
		onData(wns::service::nl::Address _address, const wns::osi::PDUPtr& _data);

	protected:
                /**
		 * @brief The configuration
		 */
		wns::pyconfig::View pyco;

		wns::node::component::Component* component;

		wns::service::nl::Notification* ipNotification;

		constanze::Listener* listener;

                /**
		 * @brief My own domain name
		 */
		wns::service::nl::FQDN listenDomainName;


		/**
		 * @brief Logger instance.
		 */
		wns::logger::Logger log;

		virtual std::string	printAddress() const;

	};
} //constanze

#endif
