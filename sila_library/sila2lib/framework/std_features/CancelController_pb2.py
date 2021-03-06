# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CancelController.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sila2lib.framework.SiLAFramework_pb2 as SiLAFramework__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='CancelController.proto',
  package='sila2.org.silastandard.core.cancelcontroller.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x43\x61ncelController.proto\x12/sila2.org.silastandard.core.cancelcontroller.v1\x1a\x13SiLAFramework.proto\"\x13\n\x11\x43\x61ncel_Parameters\"\x12\n\x10\x43\x61ncel_Responses2\xa6\x01\n\x10\x43\x61ncelController\x12\x91\x01\n\x06\x43\x61ncel\x12\x42.sila2.org.silastandard.core.cancelcontroller.v1.Cancel_Parameters\x1a\x41.sila2.org.silastandard.core.cancelcontroller.v1.Cancel_Responses\"\x00\x62\x06proto3')
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_CANCEL_PARAMETERS = _descriptor.Descriptor(
  name='Cancel_Parameters',
  full_name='sila2.org.silastandard.core.cancelcontroller.v1.Cancel_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=115,
)


_CANCEL_RESPONSES = _descriptor.Descriptor(
  name='Cancel_Responses',
  full_name='sila2.org.silastandard.core.cancelcontroller.v1.Cancel_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=135,
)

DESCRIPTOR.message_types_by_name['Cancel_Parameters'] = _CANCEL_PARAMETERS
DESCRIPTOR.message_types_by_name['Cancel_Responses'] = _CANCEL_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cancel_Parameters = _reflection.GeneratedProtocolMessageType('Cancel_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _CANCEL_PARAMETERS,
  '__module__' : 'CancelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.core.cancelcontroller.v1.Cancel_Parameters)
  })
_sym_db.RegisterMessage(Cancel_Parameters)

Cancel_Responses = _reflection.GeneratedProtocolMessageType('Cancel_Responses', (_message.Message,), {
  'DESCRIPTOR' : _CANCEL_RESPONSES,
  '__module__' : 'CancelController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.core.cancelcontroller.v1.Cancel_Responses)
  })
_sym_db.RegisterMessage(Cancel_Responses)



_CANCELCONTROLLER = _descriptor.ServiceDescriptor(
  name='CancelController',
  full_name='sila2.org.silastandard.core.cancelcontroller.v1.CancelController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=138,
  serialized_end=304,
  methods=[
  _descriptor.MethodDescriptor(
    name='Cancel',
    full_name='sila2.org.silastandard.core.cancelcontroller.v1.CancelController.Cancel',
    index=0,
    containing_service=None,
    input_type=_CANCEL_PARAMETERS,
    output_type=_CANCEL_RESPONSES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CANCELCONTROLLER)

DESCRIPTOR.services_by_name['CancelController'] = _CANCELCONTROLLER

# @@protoc_insertion_point(module_scope)
