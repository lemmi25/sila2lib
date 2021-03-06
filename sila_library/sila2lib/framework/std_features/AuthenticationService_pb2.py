# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AuthenticationService.proto

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
  name='AuthenticationService.proto',
  package='sila2.org.silastandard.core.authenticationservice.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x41uthenticationService.proto\x12\x34sila2.org.silastandard.core.authenticationservice.v1\x1a\x13SiLAFramework.proto\"\x80\x01\n\x10Login_Parameters\x12:\n\x12UserIdentification\x18\x01 \x01(\x0b\x32\x1e.sila2.org.silastandard.String\x12\x30\n\x08Password\x18\x02 \x01(\x0b\x32\x1e.sila2.org.silastandard.String\"~\n\x0fLogin_Responses\x12\x33\n\x0b\x41\x63\x63\x65ssToken\x18\x01 \x01(\x0b\x32\x1e.sila2.org.silastandard.String\x12\x36\n\rTokenLifetime\x18\x02 \x01(\x0b\x32\x1f.sila2.org.silastandard.Integer\"H\n\x11Logout_Parameters\x12\x33\n\x0b\x41\x63\x63\x65ssToken\x18\x01 \x01(\x0b\x32\x1e.sila2.org.silastandard.String\"\x12\n\x10Logout_Responses2\xd0\x02\n\x15\x41uthenticationService\x12\x98\x01\n\x05Login\x12\x46.sila2.org.silastandard.core.authenticationservice.v1.Login_Parameters\x1a\x45.sila2.org.silastandard.core.authenticationservice.v1.Login_Responses\"\x00\x12\x9b\x01\n\x06Logout\x12G.sila2.org.silastandard.core.authenticationservice.v1.Logout_Parameters\x1a\x46.sila2.org.silastandard.core.authenticationservice.v1.Logout_Responses\"\x00\x62\x06proto3')
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_LOGIN_PARAMETERS = _descriptor.Descriptor(
  name='Login_Parameters',
  full_name='sila2.org.silastandard.core.authenticationservice.v1.Login_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='UserIdentification', full_name='sila2.org.silastandard.core.authenticationservice.v1.Login_Parameters.UserIdentification', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Password', full_name='sila2.org.silastandard.core.authenticationservice.v1.Login_Parameters.Password', index=1,
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
  serialized_start=107,
  serialized_end=235,
)


_LOGIN_RESPONSES = _descriptor.Descriptor(
  name='Login_Responses',
  full_name='sila2.org.silastandard.core.authenticationservice.v1.Login_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='AccessToken', full_name='sila2.org.silastandard.core.authenticationservice.v1.Login_Responses.AccessToken', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TokenLifetime', full_name='sila2.org.silastandard.core.authenticationservice.v1.Login_Responses.TokenLifetime', index=1,
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
  serialized_start=237,
  serialized_end=363,
)


_LOGOUT_PARAMETERS = _descriptor.Descriptor(
  name='Logout_Parameters',
  full_name='sila2.org.silastandard.core.authenticationservice.v1.Logout_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='AccessToken', full_name='sila2.org.silastandard.core.authenticationservice.v1.Logout_Parameters.AccessToken', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=365,
  serialized_end=437,
)


_LOGOUT_RESPONSES = _descriptor.Descriptor(
  name='Logout_Responses',
  full_name='sila2.org.silastandard.core.authenticationservice.v1.Logout_Responses',
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
  serialized_start=439,
  serialized_end=457,
)

_LOGIN_PARAMETERS.fields_by_name['UserIdentification'].message_type = SiLAFramework__pb2._STRING
_LOGIN_PARAMETERS.fields_by_name['Password'].message_type = SiLAFramework__pb2._STRING
_LOGIN_RESPONSES.fields_by_name['AccessToken'].message_type = SiLAFramework__pb2._STRING
_LOGIN_RESPONSES.fields_by_name['TokenLifetime'].message_type = SiLAFramework__pb2._INTEGER
_LOGOUT_PARAMETERS.fields_by_name['AccessToken'].message_type = SiLAFramework__pb2._STRING
DESCRIPTOR.message_types_by_name['Login_Parameters'] = _LOGIN_PARAMETERS
DESCRIPTOR.message_types_by_name['Login_Responses'] = _LOGIN_RESPONSES
DESCRIPTOR.message_types_by_name['Logout_Parameters'] = _LOGOUT_PARAMETERS
DESCRIPTOR.message_types_by_name['Logout_Responses'] = _LOGOUT_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Login_Parameters = _reflection.GeneratedProtocolMessageType('Login_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _LOGIN_PARAMETERS,
  '__module__' : 'AuthenticationService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.core.authenticationservice.v1.Login_Parameters)
  })
_sym_db.RegisterMessage(Login_Parameters)

Login_Responses = _reflection.GeneratedProtocolMessageType('Login_Responses', (_message.Message,), {
  'DESCRIPTOR' : _LOGIN_RESPONSES,
  '__module__' : 'AuthenticationService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.core.authenticationservice.v1.Login_Responses)
  })
_sym_db.RegisterMessage(Login_Responses)

Logout_Parameters = _reflection.GeneratedProtocolMessageType('Logout_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUT_PARAMETERS,
  '__module__' : 'AuthenticationService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.core.authenticationservice.v1.Logout_Parameters)
  })
_sym_db.RegisterMessage(Logout_Parameters)

Logout_Responses = _reflection.GeneratedProtocolMessageType('Logout_Responses', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUT_RESPONSES,
  '__module__' : 'AuthenticationService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.core.authenticationservice.v1.Logout_Responses)
  })
_sym_db.RegisterMessage(Logout_Responses)



_AUTHENTICATIONSERVICE = _descriptor.ServiceDescriptor(
  name='AuthenticationService',
  full_name='sila2.org.silastandard.core.authenticationservice.v1.AuthenticationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=460,
  serialized_end=796,
  methods=[
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='sila2.org.silastandard.core.authenticationservice.v1.AuthenticationService.Login',
    index=0,
    containing_service=None,
    input_type=_LOGIN_PARAMETERS,
    output_type=_LOGIN_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Logout',
    full_name='sila2.org.silastandard.core.authenticationservice.v1.AuthenticationService.Logout',
    index=1,
    containing_service=None,
    input_type=_LOGOUT_PARAMETERS,
    output_type=_LOGOUT_RESPONSES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHENTICATIONSERVICE)

DESCRIPTOR.services_by_name['AuthenticationService'] = _AUTHENTICATIONSERVICE

# @@protoc_insertion_point(module_scope)
