# coding: utf-8

"""
    HPC Web API

    Preview  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from hpc_acm.models.scheduled_event import ScheduledEvent  # noqa: F401,E501


class ScheduledEvents(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'document_incarnation': 'int',
        'events': 'list[ScheduledEvent]'
    }

    attribute_map = {
        'document_incarnation': 'documentIncarnation',
        'events': 'events'
    }

    def __init__(self, document_incarnation=None, events=None):  # noqa: E501
        """ScheduledEvents - a model defined in Swagger"""  # noqa: E501

        self._document_incarnation = None
        self._events = None
        self.discriminator = None

        if document_incarnation is not None:
            self.document_incarnation = document_incarnation
        if events is not None:
            self.events = events

    @property
    def document_incarnation(self):
        """Gets the document_incarnation of this ScheduledEvents.  # noqa: E501


        :return: The document_incarnation of this ScheduledEvents.  # noqa: E501
        :rtype: int
        """
        return self._document_incarnation

    @document_incarnation.setter
    def document_incarnation(self, document_incarnation):
        """Sets the document_incarnation of this ScheduledEvents.


        :param document_incarnation: The document_incarnation of this ScheduledEvents.  # noqa: E501
        :type: int
        """

        self._document_incarnation = document_incarnation

    @property
    def events(self):
        """Gets the events of this ScheduledEvents.  # noqa: E501


        :return: The events of this ScheduledEvents.  # noqa: E501
        :rtype: list[ScheduledEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ScheduledEvents.


        :param events: The events of this ScheduledEvents.  # noqa: E501
        :type: list[ScheduledEvent]
        """

        self._events = events

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScheduledEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
