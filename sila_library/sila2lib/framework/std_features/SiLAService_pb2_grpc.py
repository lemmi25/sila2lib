# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import SiLAService_pb2 as SiLAService__pb2


class SiLAServiceStub(object):
  """Feature: SiLA Service

  The Feature each SiLA Server MUST implement. It is the entry point to a SiLA Server and helps to discover the
  Features it implements.

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeatureDefinition = channel.unary_unary(
        '/sila2.org.silastandard.core.silaservice.v1.SiLAService/GetFeatureDefinition',
        request_serializer=SiLAService__pb2.GetFeatureDefinition_Parameters.SerializeToString,
        response_deserializer=SiLAService__pb2.GetFeatureDefinition_Responses.FromString,
        )
    self.SetServerName = channel.unary_unary(
        '/sila2.org.silastandard.core.silaservice.v1.SiLAService/SetServerName',
        request_serializer=SiLAService__pb2.SetServerName_Parameters.SerializeToString,
        response_deserializer=SiLAService__pb2.SetServerName_Responses.FromString,
        )
    self.Get_ServerName = channel.unary_unary(
        '/sila2.org.silastandard.core.silaservice.v1.SiLAService/Get_ServerName',
        request_serializer=SiLAService__pb2.Get_ServerName_Parameters.SerializeToString,
        response_deserializer=SiLAService__pb2.Get_ServerName_Responses.FromString,
        )
    self.Get_ServerType = channel.unary_unary(
        '/sila2.org.silastandard.core.silaservice.v1.SiLAService/Get_ServerType',
        request_serializer=SiLAService__pb2.Get_ServerType_Parameters.SerializeToString,
        response_deserializer=SiLAService__pb2.Get_ServerType_Responses.FromString,
        )
    self.Get_ServerUUID = channel.unary_unary(
        '/sila2.org.silastandard.core.silaservice.v1.SiLAService/Get_ServerUUID',
        request_serializer=SiLAService__pb2.Get_ServerUUID_Parameters.SerializeToString,
        response_deserializer=SiLAService__pb2.Get_ServerUUID_Responses.FromString,
        )
    self.Get_ServerDescription = channel.unary_unary(
        '/sila2.org.silastandard.core.silaservice.v1.SiLAService/Get_ServerDescription',
        request_serializer=SiLAService__pb2.Get_ServerDescription_Parameters.SerializeToString,
        response_deserializer=SiLAService__pb2.Get_ServerDescription_Responses.FromString,
        )
    self.Get_ServerVersion = channel.unary_unary(
        '/sila2.org.silastandard.core.silaservice.v1.SiLAService/Get_ServerVersion',
        request_serializer=SiLAService__pb2.Get_ServerVersion_Parameters.SerializeToString,
        response_deserializer=SiLAService__pb2.Get_ServerVersion_Responses.FromString,
        )
    self.Get_ServerVendorURL = channel.unary_unary(
        '/sila2.org.silastandard.core.silaservice.v1.SiLAService/Get_ServerVendorURL',
        request_serializer=SiLAService__pb2.Get_ServerVendorURL_Parameters.SerializeToString,
        response_deserializer=SiLAService__pb2.Get_ServerVendorURL_Responses.FromString,
        )
    self.Get_ImplementedFeatures = channel.unary_unary(
        '/sila2.org.silastandard.core.silaservice.v1.SiLAService/Get_ImplementedFeatures',
        request_serializer=SiLAService__pb2.Get_ImplementedFeatures_Parameters.SerializeToString,
        response_deserializer=SiLAService__pb2.Get_ImplementedFeatures_Responses.FromString,
        )


class SiLAServiceServicer(object):
  """Feature: SiLA Service

  The Feature each SiLA Server MUST implement. It is the entry point to a SiLA Server and helps to discover the
  Features it implements.

  """

  def GetFeatureDefinition(self, request, context):
    """Get Feature Definition
    Get all details on one Feature through the qualified Feature id.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetServerName(self, request, context):
    """Set Server Name
    Sets a human readable name to the Server Name property
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get_ServerName(self, request, context):
    """Server Name
    Human readable name of the SiLA Server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get_ServerType(self, request, context):
    """Server Type
    The type of Server this is. Is specified by the implementer of the server and not unique.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get_ServerUUID(self, request, context):
    """Server UUID
    Globally unique identifier that identifies a SiLA Server. The Server UUID MUST
    be generated once and always remain the same.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get_ServerDescription(self, request, context):
    """Server Description
    Description of the SiLA Server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get_ServerVersion(self, request, context):
    """Server Version

    Returns the version of the SiLA Server. A "Major" and a "Minor" version number (e.g. 1.0) MUST be provided,
    a Patch version number MAY be provided. Optionally, an arbitrary text, separated by an underscore MAY be
    appended,
    e.g. ???3.19.373_mighty_lab_devices???

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get_ServerVendorURL(self, request, context):
    """Server Vendor URL

    Returns the URL to the website of the vendor or the website
    of the product of this SiLA Server.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get_ImplementedFeatures(self, request, context):
    """Implemented Features

    Returns a list of qualified Feature identifiers of all
    implemented Features of this SiLA Server.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SiLAServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeatureDefinition': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeatureDefinition,
          request_deserializer=SiLAService__pb2.GetFeatureDefinition_Parameters.FromString,
          response_serializer=SiLAService__pb2.GetFeatureDefinition_Responses.SerializeToString,
      ),
      'SetServerName': grpc.unary_unary_rpc_method_handler(
          servicer.SetServerName,
          request_deserializer=SiLAService__pb2.SetServerName_Parameters.FromString,
          response_serializer=SiLAService__pb2.SetServerName_Responses.SerializeToString,
      ),
      'Get_ServerName': grpc.unary_unary_rpc_method_handler(
          servicer.Get_ServerName,
          request_deserializer=SiLAService__pb2.Get_ServerName_Parameters.FromString,
          response_serializer=SiLAService__pb2.Get_ServerName_Responses.SerializeToString,
      ),
      'Get_ServerType': grpc.unary_unary_rpc_method_handler(
          servicer.Get_ServerType,
          request_deserializer=SiLAService__pb2.Get_ServerType_Parameters.FromString,
          response_serializer=SiLAService__pb2.Get_ServerType_Responses.SerializeToString,
      ),
      'Get_ServerUUID': grpc.unary_unary_rpc_method_handler(
          servicer.Get_ServerUUID,
          request_deserializer=SiLAService__pb2.Get_ServerUUID_Parameters.FromString,
          response_serializer=SiLAService__pb2.Get_ServerUUID_Responses.SerializeToString,
      ),
      'Get_ServerDescription': grpc.unary_unary_rpc_method_handler(
          servicer.Get_ServerDescription,
          request_deserializer=SiLAService__pb2.Get_ServerDescription_Parameters.FromString,
          response_serializer=SiLAService__pb2.Get_ServerDescription_Responses.SerializeToString,
      ),
      'Get_ServerVersion': grpc.unary_unary_rpc_method_handler(
          servicer.Get_ServerVersion,
          request_deserializer=SiLAService__pb2.Get_ServerVersion_Parameters.FromString,
          response_serializer=SiLAService__pb2.Get_ServerVersion_Responses.SerializeToString,
      ),
      'Get_ServerVendorURL': grpc.unary_unary_rpc_method_handler(
          servicer.Get_ServerVendorURL,
          request_deserializer=SiLAService__pb2.Get_ServerVendorURL_Parameters.FromString,
          response_serializer=SiLAService__pb2.Get_ServerVendorURL_Responses.SerializeToString,
      ),
      'Get_ImplementedFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.Get_ImplementedFeatures,
          request_deserializer=SiLAService__pb2.Get_ImplementedFeatures_Parameters.FromString,
          response_serializer=SiLAService__pb2.Get_ImplementedFeatures_Responses.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sila2.org.silastandard.core.silaservice.v1.SiLAService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
