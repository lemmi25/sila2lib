# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import LockController_pb2 as LockController__pb2


class LockControllerStub(object):
  """Feature: Lock Controller

  This Feature allows a SiLA Client to lock a SiLA Server for exclusive use, preventing other SiLA Clients from
  using the server while it is locked. To lock a SiLA Server a lock identifier has to be set, using the
  'LockServer' command. This identifier has to be sent along with every (lock protected) request to the SiLA
  Server in
  order to use it's functionality.

  To send the lock identifier the SiLA Client Meta Data 'LockIdentifier' has to be used.
  When locking a SiLA Server a timeout can be specified that defines the time after which the SiLA Server will
  be automatically unlocked if no request with a valid lock identifier has been received meanwhile. After the
  timeout has
  expired or after explicit unlock no lock identifier has to be sent any more.

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.LockServer = channel.unary_unary(
        '/sila2.org.silastandard.core.lockcontroller.v1.LockController/LockServer',
        request_serializer=LockController__pb2.LockServer_Parameters.SerializeToString,
        response_deserializer=LockController__pb2.LockServer_Responses.FromString,
        )
    self.UnlockServer = channel.unary_unary(
        '/sila2.org.silastandard.core.lockcontroller.v1.LockController/UnlockServer',
        request_serializer=LockController__pb2.UnlockServer_Parameters.SerializeToString,
        response_deserializer=LockController__pb2.UnlockServer_Responses.FromString,
        )
    self.Get_IsLocked = channel.unary_unary(
        '/sila2.org.silastandard.core.lockcontroller.v1.LockController/Get_IsLocked',
        request_serializer=LockController__pb2.Get_IsLocked_Parameters.SerializeToString,
        response_deserializer=LockController__pb2.Get_IsLocked_Responses.FromString,
        )
    self.Get_FCPAffectedByMetadata_LockIdentifier = channel.unary_unary(
        '/sila2.org.silastandard.core.lockcontroller.v1.LockController/Get_FCPAffectedByMetadata_LockIdentifier',
        request_serializer=LockController__pb2.Get_FCPAffectedByMetadata_LockIdentifier_Parameters.SerializeToString,
        response_deserializer=LockController__pb2.Get_FCPAffectedByMetadata_LockIdentifier_Responses.FromString,
        )


class LockControllerServicer(object):
  """Feature: Lock Controller

  This Feature allows a SiLA Client to lock a SiLA Server for exclusive use, preventing other SiLA Clients from
  using the server while it is locked. To lock a SiLA Server a lock identifier has to be set, using the
  'LockServer' command. This identifier has to be sent along with every (lock protected) request to the SiLA
  Server in
  order to use it's functionality.

  To send the lock identifier the SiLA Client Meta Data 'LockIdentifier' has to be used.
  When locking a SiLA Server a timeout can be specified that defines the time after which the SiLA Server will
  be automatically unlocked if no request with a valid lock identifier has been received meanwhile. After the
  timeout has
  expired or after explicit unlock no lock identifier has to be sent any more.

  """

  def LockServer(self, request, context):
    """Lock Server

    Locks a SiLA Server for exclusive use by setting a lock identifier that has to be sent along with
    any following (lock protected) request as long as the SiLA Server is locked.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnlockServer(self, request, context):
    """Unlock Server

    Unlocks a locked SiLA Server. No lock identifier has to be sent for any following calls until
    the server is locked again.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get_IsLocked(self, request, context):
    """IsLocked

    Returns true if the SiLA Server is currently locked or false else.

    This property MUST NOT be lock protected, so that any SiLA Client can query the current lock state
    of a SiLA Server.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get_FCPAffectedByMetadata_LockIdentifier(self, request, context):
    """Lock Identifier
    The lock identifier has to be sent with every (lock protected) call in order to use the functionality of a locked SiLA
    Server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LockControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'LockServer': grpc.unary_unary_rpc_method_handler(
          servicer.LockServer,
          request_deserializer=LockController__pb2.LockServer_Parameters.FromString,
          response_serializer=LockController__pb2.LockServer_Responses.SerializeToString,
      ),
      'UnlockServer': grpc.unary_unary_rpc_method_handler(
          servicer.UnlockServer,
          request_deserializer=LockController__pb2.UnlockServer_Parameters.FromString,
          response_serializer=LockController__pb2.UnlockServer_Responses.SerializeToString,
      ),
      'Get_IsLocked': grpc.unary_unary_rpc_method_handler(
          servicer.Get_IsLocked,
          request_deserializer=LockController__pb2.Get_IsLocked_Parameters.FromString,
          response_serializer=LockController__pb2.Get_IsLocked_Responses.SerializeToString,
      ),
      'Get_FCPAffectedByMetadata_LockIdentifier': grpc.unary_unary_rpc_method_handler(
          servicer.Get_FCPAffectedByMetadata_LockIdentifier,
          request_deserializer=LockController__pb2.Get_FCPAffectedByMetadata_LockIdentifier_Parameters.FromString,
          response_serializer=LockController__pb2.Get_FCPAffectedByMetadata_LockIdentifier_Responses.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sila2.org.silastandard.core.lockcontroller.v1.LockController', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))