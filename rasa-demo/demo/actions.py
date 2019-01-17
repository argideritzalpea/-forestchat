# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from typing import Text, Dict, Any, List

from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, \
    ConversationPaused, FollowupAction, Form

from demo.api import MailChimpAPI
from demo import config
from demo.gdrive_service import GDriveService

logger = logging.getLogger(__name__)


class ActionStoreInSpreadsheet(Action):
    """Saves the time of the count into a spreadsheet"""

    def name(self):
        return "action_store_CountTime"

    def run(self, dispatcher, tracker, domain):
        import datetime
        countTime = tracker.get_slot('countTime')
        peopleCount = tracker.get_slot('peopleCount')
        vehicleCount = tracker.get_slot('vehicleCount')
        trailVisits = tracker.get_slot('trailVisits')
        returnStatus = tracker.get_slot('returnStatus')
        infoSource = tracker.get_slot('infoSource')
        zipCode = tracker.get_slot('zipCode')
        yearBorn = tracker.get_slot('yearBorn')

        date_cur = datetime.datetime.now().strftime("%d/%m/%Y")

        time = [data_cur, countTime, peopleCount, vehicleCount, trailVisits,
        returnStatus, infoSource, zipCode, yearBorn]

        gdrive = GDriveService()
        try:
            gdrive.store_data(sales_info)
            return [SlotSet('data_stored', True)]
        except Exception as e:
            logger.error("Failed to write data to gdocs. Error: {}"
                         "".format(e.message), exc_info=True)
            return [SlotSet('data_stored', False)]


class ActionStorePeopleCount(Action):
    """Stores the number of people in a party in a slot"""

    def name(self):
        return "action_store_PeopleCount"

    def run(self, dispatcher, tracker, domain):

        peopleCount = next(tracker.get_latest_entity_values('number'), None)

        if peopleCount:
            return [SlotSet('peopleCount', peopleCount)]
        else:
            return []

class ActionStoreVehicleCount(Action):
    """Stores the number of vehicles in a party in a slot"""

    def name(self):
        return "action_store_VehicleCount"

    def run(self, dispatcher, tracker, domain):

        vehicleCount = next(tracker.get_latest_entity_values('number'), None)

        if vehicleCount:
            return [SlotSet('vehicleCount', vehicleCount)]
        else:
            return []


class ActionStoreCountTime(Action):
    """Stores time at which count was conducted in a slot"""

    def name(self):
        return "action_store_CountTime"

    def run(self, dispatcher, tracker, domain):

        countTime = next(tracker.get_latest_entity_values('text'), None)

        if countTime:
            return [SlotSet('countTime', countTime)]
        else:
            return []

class ActionStoreReturnStatus(Action):
    """Stores whether returning or leaving in a slot"""

    def name(self):
        return "action_store_ReturnStatus"

    def run(self, dispatcher, tracker, domain):

        returnStatus = next(tracker.get_latest_entity_values('returnStatus'), None)

        if returnStatus:
            return [SlotSet('returnStatus', returnStatus)]
        else:
            return []

class ActionStoreTrailVisits(Action):
    """Stores number of trail visits in past year in a slot"""

    def name(self):
        return "action_store_TrailVisits"

    def run(self, dispatcher, tracker, domain):

        trailVisits = next(tracker.get_latest_entity_values('number'), None)

        if trailVisits:
            return [SlotSet('trailVisits', trailVisits)]
        else:
            return []


class ActionStoreYearBorn(Action):
    """Stores year born in a slot"""

    def name(self):
        return "action_store_YearBorn"

    def run(self, dispatcher, tracker, domain):

        yearBorn = next(tracker.get_latest_entity_values('year'), None)

        if yearBorn:
            return [SlotSet('yearBorn', yearBorn)]
        else:
            return []


class ActionStoreZipCode(Action):
    """Stores zip code in a slot"""

    def name(self):
        return "action_store_ZipCode"

    def run(self, dispatcher, tracker, domain):

        zipCode = next(tracker.get_latest_entity_values('number'), None)

        if trailVisits:
            return [SlotSet('zipCode', zipCode)]
        else:
            return []
