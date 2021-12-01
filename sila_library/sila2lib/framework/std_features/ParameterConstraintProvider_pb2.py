# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ParameterConstraintProvider.proto

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
  name='ParameterConstraintProvider.proto',
  package='sila2.org.silastandard.core.parameterconstraintsprovider.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!ParameterConstraintProvider.proto\x12;sila2.org.silastandard.core.parameterconstraintsprovider.v1\x1a\x13SiLAFramework.proto\",\n*Subscribe_ParametersConstraints_Parameters\"\xeb\x02\n)Subscribe_ParametersConstraints_Responses\x12\xa3\x01\n\x15ParametersConstraints\x18\x01 \x03(\x0b\x32\x83\x01.sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Responses.ParametersConstraints_Struct\x1a\x97\x01\n\x1cParametersConstraints_Struct\x12\x42\n\x1a\x43ommandParameterIdentifier\x18\x01 \x01(\x0b\x32\x1e.sila2.org.silastandard.String\x12\x33\n\x0b\x43onstraints\x18\x02 \x01(\x0b\x32\x1e.sila2.org.silastandard.String2\x97\x02\n\x1cParameterConstraintsProvider\x12\xf6\x01\n\x1fSubscribe_ParametersConstraints\x12g.sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Parameters\x1a\x66.sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Responses\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_SUBSCRIBE_PARAMETERSCONSTRAINTS_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_ParametersConstraints_Parameters',
  full_name='sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Parameters',
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
  serialized_start=119,
  serialized_end=163,
)


_SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES_PARAMETERSCONSTRAINTS_STRUCT = _descriptor.Descriptor(
  name='ParametersConstraints_Struct',
  full_name='sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Responses.ParametersConstraints_Struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='CommandParameterIdentifier', full_name='sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Responses.ParametersConstraints_Struct.CommandParameterIdentifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Constraints', full_name='sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Responses.ParametersConstraints_Struct.Constraints', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=378,
  serialized_end=529,
)

_SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_ParametersConstraints_Responses',
  full_name='sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ParametersConstraints', full_name='sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Responses.ParametersConstraints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES_PARAMETERSCONSTRAINTS_STRUCT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=529,
)

_SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES_PARAMETERSCONSTRAINTS_STRUCT.fields_by_name['CommandParameterIdentifier'].message_type = SiLAFramework__pb2._STRING
_SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES_PARAMETERSCONSTRAINTS_STRUCT.fields_by_name['Constraints'].message_type = SiLAFramework__pb2._STRING
_SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES_PARAMETERSCONSTRAINTS_STRUCT.containing_type = _SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES
_SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES.fields_by_name['ParametersConstraints'].message_type = _SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES_PARAMETERSCONSTRAINTS_STRUCT
DESCRIPTOR.message_types_by_name['Subscribe_ParametersConstraints_Parameters'] = _SUBSCRIBE_PARAMETERSCONSTRAINTS_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_ParametersConstraints_Responses'] = _SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Subscribe_ParametersConstraints_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_ParametersConstraints_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_PARAMETERSCONSTRAINTS_PARAMETERS,
  '__module__' : 'ParameterConstraintProvider_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_ParametersConstraints_Parameters)

Subscribe_ParametersConstraints_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_ParametersConstraints_Responses', (_message.Message,), {

  'ParametersConstraints_Struct' : _reflection.GeneratedProtocolMessageType('ParametersConstraints_Struct', (_message.Message,), {
    'DESCRIPTOR' : _SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES_PARAMETERSCONSTRAINTS_STRUCT,
    '__module__' : 'ParameterConstraintProvider_pb2'
    # @@protoc_insertion_point(class_scope:sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Responses.ParametersConstraints_Struct)
    })
  ,
  'DESCRIPTOR' : _SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES,
  '__module__' : 'ParameterConstraintProvider_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.core.parameterconstraintsprovider.v1.Subscribe_ParametersConstraints_Responses)
  })
_sym_db.RegisterMessage(Subscribe_ParametersConstraints_Responses)
_sym_db.RegisterMessage(Subscribe_ParametersConstraints_Responses.ParametersConstraints_Struct)



_PARAMETERCONSTRAINTSPROVIDER = _descriptor.ServiceDescriptor(
  name='ParameterConstraintsProvider',
  full_name='sila2.org.silastandard.core.parameterconstraintsprovider.v1.ParameterConstraintsProvider',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=532,
  serialized_end=811,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe_ParametersConstraints',
    full_name='sila2.org.silastandard.core.parameterconstraintsprovider.v1.ParameterConstraintsProvider.Subscribe_ParametersConstraints',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBE_PARAMETERSCONSTRAINTS_PARAMETERS,
    output_type=_SUBSCRIBE_PARAMETERSCONSTRAINTS_RESPONSES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PARAMETERCONSTRAINTSPROVIDER)

DESCRIPTOR.services_by_name['ParameterConstraintsProvider'] = _PARAMETERCONSTRAINTSPROVIDER

# @@protoc_insertion_point(module_scope)
