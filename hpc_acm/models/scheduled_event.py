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


class ScheduledEvent(object):
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
        'event_id': 'str',
        'event_type': 'str',
        'resource_type': 'str',
        'resources': 'list[str]',
        'event_status': 'str',
        'not_before': 'datetime'
    }

    attribute_map = {
        'event_id': 'eventId',
        'event_type': 'eventType',
        'resource_type': 'resourceType',
        'resources': 'resources',
        'event_status': 'eventStatus',
        'not_before': 'notBefore'
    }

    def __init__(self, event_id=None, event_type=None, resource_type=None, resources=None, event_status=None, not_before=None):  # noqa: E501
        """ScheduledEvent - a model defined in Swagger"""  # noqa: E501

        self._event_id = None
        self._event_type = None
        self._resource_type = None
        self._resources = None
        self._event_status = None
        self._not_before = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if event_type is not None:
            self.event_type = event_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resources is not None:
            self.resources = resources
        if event_status is not None:
            self.event_status = event_status
        if not_before is not None:
            self.not_before = not_before

    @property
    def event_id(self):
        """Gets the event_id of this ScheduledEvent.  # noqa: E501

        Globally unique identifier for this event  # noqa: E501

        :return: The event_id of this ScheduledEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ScheduledEvent.

        Globally unique identifier for this event  # noqa: E501

        :param event_id: The event_id of this ScheduledEvent.  # noqa: E501
        :type: str
        """

        self._event_id = event_id

    @property
    def event_type(self):
        """Gets the event_type of this ScheduledEvent.  # noqa: E501

        Impact this event causes  # noqa: E501

        :return: The event_type of this ScheduledEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ScheduledEvent.

        Impact this event causes  # noqa: E501

        :param event_type: The event_type of this ScheduledEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["Freeze", "Reboot", "Redeploy"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def resource_type(self):
        """Gets the resource_type of this ScheduledEvent.  # noqa: E501

        Type of resource this event impacts  # noqa: E501

        :return: The resource_type of this ScheduledEvent.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ScheduledEvent.

        Type of resource this event impacts  # noqa: E501

        :param resource_type: The resource_type of this ScheduledEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["VirtualMachine"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def resources(self):
        """Gets the resources of this ScheduledEvent.  # noqa: E501

        List of resources this event impacts. This is guaranteed to contain machines from at most one Update Domain, but may not contain all machines in the UD.  # noqa: E501

        :return: The resources of this ScheduledEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ScheduledEvent.

        List of resources this event impacts. This is guaranteed to contain machines from at most one Update Domain, but may not contain all machines in the UD.  # noqa: E501

        :param resources: The resources of this ScheduledEvent.  # noqa: E501
        :type: list[str]
        """

        self._resources = resources

    @property
    def event_status(self):
        """Gets the event_status of this ScheduledEvent.  # noqa: E501

        No Completed or similar status is ever provided; the event will no longer be returned when the event is completed.  # noqa: E501

        :return: The event_status of this ScheduledEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """Sets the event_status of this ScheduledEvent.

        No Completed or similar status is ever provided; the event will no longer be returned when the event is completed.  # noqa: E501

        :param event_status: The event_status of this ScheduledEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["Scheduled", "Started"]  # noqa: E501
        if event_status not in allowed_values:
            raise ValueError(
                "Invalid value for `event_status` ({0}), must be one of {1}"  # noqa: E501
                .format(event_status, allowed_values)
            )

        self._event_status = event_status

    @property
    def not_before(self):
        """Gets the not_before of this ScheduledEvent.  # noqa: E501

        Time after which this event may start  # noqa: E501

        :return: The not_before of this ScheduledEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this ScheduledEvent.

        Time after which this event may start  # noqa: E501

        :param not_before: The not_before of this ScheduledEvent.  # noqa: E501
        :type: datetime
        """

        self._not_before = not_before

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
        if not isinstance(other, ScheduledEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
