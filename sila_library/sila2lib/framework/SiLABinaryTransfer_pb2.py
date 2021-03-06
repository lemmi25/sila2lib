# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SiLABinaryTransfer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import SiLAFramework_pb2 as SiLAFramework__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='SiLABinaryTransfer.proto',
  package='sila2.org.silastandard',
  syntax='proto3',
  serialized_options=_b('B\022SiLABinaryTransfer'),
  serialized_pb=_b('\n\x18SiLABinaryTransfer.proto\x12\x16sila2.org.silastandard\x1a\x13SiLAFramework.proto\"Z\n\x13\x43reateBinaryRequest\x12\x12\n\nbinarySize\x18\x01 \x01(\x04\x12\x12\n\nchunkCount\x18\x02 \x01(\r\x12\x1b\n\x13parameterIdentifier\x18\x03 \x01(\t\"n\n\x14\x43reateBinaryResponse\x12\x1a\n\x12\x62inaryTransferUUID\x18\x01 \x01(\t\x12:\n\x10lifetimeOfBinary\x18\x02 \x01(\x0b\x32 .sila2.org.silastandard.Duration\"U\n\x12UploadChunkRequest\x12\x1a\n\x12\x62inaryTransferUUID\x18\x01 \x01(\t\x12\x12\n\nchunkIndex\x18\x02 \x01(\r\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"\x81\x01\n\x13UploadChunkResponse\x12\x1a\n\x12\x62inaryTransferUUID\x18\x01 \x01(\t\x12\x12\n\nchunkIndex\x18\x02 \x01(\r\x12:\n\x10lifetimeOfBinary\x18\x03 \x01(\x0b\x32 .sila2.org.silastandard.Duration\"1\n\x13\x44\x65leteBinaryRequest\x12\x1a\n\x12\x62inaryTransferUUID\x18\x01 \x01(\t\"\x16\n\x14\x44\x65leteBinaryResponse\"2\n\x14GetBinaryInfoRequest\x12\x1a\n\x12\x62inaryTransferUUID\x18\x01 \x01(\t\"g\n\x15GetBinaryInfoResponse\x12\x12\n\nbinarySize\x18\x01 \x01(\x04\x12:\n\x10lifetimeOfBinary\x18\x02 \x01(\x0b\x32 .sila2.org.silastandard.Duration\"M\n\x0fGetChunkRequest\x12\x1a\n\x12\x62inaryTransferUUID\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0e\n\x06length\x18\x03 \x01(\r\"\x8b\x01\n\x10GetChunkResponse\x12\x1a\n\x12\x62inaryTransferUUID\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12:\n\x10lifetimeOfBinary\x18\x04 \x01(\x0b\x32 .sila2.org.silastandard.Duration\"\xd5\x01\n\x13\x42inaryTransferError\x12H\n\terrorType\x18\x01 \x01(\x0e\x32\x35.sila2.org.silastandard.BinaryTransferError.ErrorType\x12\x0f\n\x07message\x18\x02 \x01(\t\"c\n\tErrorType\x12 \n\x1cINVALID_BINARY_TRANSFER_UUID\x10\x00\x12\x18\n\x14\x42INARY_UPLOAD_FAILED\x10\x01\x12\x1a\n\x16\x42INARY_DOWNLOAD_FAILED\x10\x02\x32\xd6\x02\n\x0c\x42inaryUpload\x12k\n\x0c\x43reateBinary\x12+.sila2.org.silastandard.CreateBinaryRequest\x1a,.sila2.org.silastandard.CreateBinaryResponse\"\x00\x12l\n\x0bUploadChunk\x12*.sila2.org.silastandard.UploadChunkRequest\x1a+.sila2.org.silastandard.UploadChunkResponse\"\x00(\x01\x30\x01\x12k\n\x0c\x44\x65leteBinary\x12+.sila2.org.silastandard.DeleteBinaryRequest\x1a,.sila2.org.silastandard.DeleteBinaryResponse\"\x00\x32\xd2\x02\n\x0e\x42inaryDownload\x12n\n\rGetBinaryInfo\x12,.sila2.org.silastandard.GetBinaryInfoRequest\x1a-.sila2.org.silastandard.GetBinaryInfoResponse\"\x00\x12\x63\n\x08GetChunk\x12\'.sila2.org.silastandard.GetChunkRequest\x1a(.sila2.org.silastandard.GetChunkResponse\"\x00(\x01\x30\x01\x12k\n\x0c\x44\x65leteBinary\x12+.sila2.org.silastandard.DeleteBinaryRequest\x1a,.sila2.org.silastandard.DeleteBinaryResponse\"\x00\x42\x14\x42\x12SiLABinaryTransferb\x06proto3')
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])



_BINARYTRANSFERERROR_ERRORTYPE = _descriptor.EnumDescriptor(
  name='ErrorType',
  full_name='sila2.org.silastandard.BinaryTransferError.ErrorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_BINARY_TRANSFER_UUID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINARY_UPLOAD_FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINARY_DOWNLOAD_FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1064,
  serialized_end=1163,
)
_sym_db.RegisterEnumDescriptor(_BINARYTRANSFERERROR_ERRORTYPE)


_CREATEBINARYREQUEST = _descriptor.Descriptor(
  name='CreateBinaryRequest',
  full_name='sila2.org.silastandard.CreateBinaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binarySize', full_name='sila2.org.silastandard.CreateBinaryRequest.binarySize', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunkCount', full_name='sila2.org.silastandard.CreateBinaryRequest.chunkCount', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameterIdentifier', full_name='sila2.org.silastandard.CreateBinaryRequest.parameterIdentifier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=73,
  serialized_end=163,
)


_CREATEBINARYRESPONSE = _descriptor.Descriptor(
  name='CreateBinaryResponse',
  full_name='sila2.org.silastandard.CreateBinaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binaryTransferUUID', full_name='sila2.org.silastandard.CreateBinaryResponse.binaryTransferUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetimeOfBinary', full_name='sila2.org.silastandard.CreateBinaryResponse.lifetimeOfBinary', index=1,
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
  serialized_start=165,
  serialized_end=275,
)


_UPLOADCHUNKREQUEST = _descriptor.Descriptor(
  name='UploadChunkRequest',
  full_name='sila2.org.silastandard.UploadChunkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binaryTransferUUID', full_name='sila2.org.silastandard.UploadChunkRequest.binaryTransferUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunkIndex', full_name='sila2.org.silastandard.UploadChunkRequest.chunkIndex', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='sila2.org.silastandard.UploadChunkRequest.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=277,
  serialized_end=362,
)


_UPLOADCHUNKRESPONSE = _descriptor.Descriptor(
  name='UploadChunkResponse',
  full_name='sila2.org.silastandard.UploadChunkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binaryTransferUUID', full_name='sila2.org.silastandard.UploadChunkResponse.binaryTransferUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunkIndex', full_name='sila2.org.silastandard.UploadChunkResponse.chunkIndex', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetimeOfBinary', full_name='sila2.org.silastandard.UploadChunkResponse.lifetimeOfBinary', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_end=494,
)


_DELETEBINARYREQUEST = _descriptor.Descriptor(
  name='DeleteBinaryRequest',
  full_name='sila2.org.silastandard.DeleteBinaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binaryTransferUUID', full_name='sila2.org.silastandard.DeleteBinaryRequest.binaryTransferUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=496,
  serialized_end=545,
)


_DELETEBINARYRESPONSE = _descriptor.Descriptor(
  name='DeleteBinaryResponse',
  full_name='sila2.org.silastandard.DeleteBinaryResponse',
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
  serialized_start=547,
  serialized_end=569,
)


_GETBINARYINFOREQUEST = _descriptor.Descriptor(
  name='GetBinaryInfoRequest',
  full_name='sila2.org.silastandard.GetBinaryInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binaryTransferUUID', full_name='sila2.org.silastandard.GetBinaryInfoRequest.binaryTransferUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=571,
  serialized_end=621,
)


_GETBINARYINFORESPONSE = _descriptor.Descriptor(
  name='GetBinaryInfoResponse',
  full_name='sila2.org.silastandard.GetBinaryInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binarySize', full_name='sila2.org.silastandard.GetBinaryInfoResponse.binarySize', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetimeOfBinary', full_name='sila2.org.silastandard.GetBinaryInfoResponse.lifetimeOfBinary', index=1,
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
  serialized_start=623,
  serialized_end=726,
)


_GETCHUNKREQUEST = _descriptor.Descriptor(
  name='GetChunkRequest',
  full_name='sila2.org.silastandard.GetChunkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binaryTransferUUID', full_name='sila2.org.silastandard.GetChunkRequest.binaryTransferUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='sila2.org.silastandard.GetChunkRequest.offset', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='sila2.org.silastandard.GetChunkRequest.length', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=728,
  serialized_end=805,
)


_GETCHUNKRESPONSE = _descriptor.Descriptor(
  name='GetChunkResponse',
  full_name='sila2.org.silastandard.GetChunkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binaryTransferUUID', full_name='sila2.org.silastandard.GetChunkResponse.binaryTransferUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='sila2.org.silastandard.GetChunkResponse.offset', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='sila2.org.silastandard.GetChunkResponse.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetimeOfBinary', full_name='sila2.org.silastandard.GetChunkResponse.lifetimeOfBinary', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=808,
  serialized_end=947,
)


_BINARYTRANSFERERROR = _descriptor.Descriptor(
  name='BinaryTransferError',
  full_name='sila2.org.silastandard.BinaryTransferError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='errorType', full_name='sila2.org.silastandard.BinaryTransferError.errorType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='sila2.org.silastandard.BinaryTransferError.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BINARYTRANSFERERROR_ERRORTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=950,
  serialized_end=1163,
)

_CREATEBINARYRESPONSE.fields_by_name['lifetimeOfBinary'].message_type = SiLAFramework__pb2._DURATION
_UPLOADCHUNKRESPONSE.fields_by_name['lifetimeOfBinary'].message_type = SiLAFramework__pb2._DURATION
_GETBINARYINFORESPONSE.fields_by_name['lifetimeOfBinary'].message_type = SiLAFramework__pb2._DURATION
_GETCHUNKRESPONSE.fields_by_name['lifetimeOfBinary'].message_type = SiLAFramework__pb2._DURATION
_BINARYTRANSFERERROR.fields_by_name['errorType'].enum_type = _BINARYTRANSFERERROR_ERRORTYPE
_BINARYTRANSFERERROR_ERRORTYPE.containing_type = _BINARYTRANSFERERROR
DESCRIPTOR.message_types_by_name['CreateBinaryRequest'] = _CREATEBINARYREQUEST
DESCRIPTOR.message_types_by_name['CreateBinaryResponse'] = _CREATEBINARYRESPONSE
DESCRIPTOR.message_types_by_name['UploadChunkRequest'] = _UPLOADCHUNKREQUEST
DESCRIPTOR.message_types_by_name['UploadChunkResponse'] = _UPLOADCHUNKRESPONSE
DESCRIPTOR.message_types_by_name['DeleteBinaryRequest'] = _DELETEBINARYREQUEST
DESCRIPTOR.message_types_by_name['DeleteBinaryResponse'] = _DELETEBINARYRESPONSE
DESCRIPTOR.message_types_by_name['GetBinaryInfoRequest'] = _GETBINARYINFOREQUEST
DESCRIPTOR.message_types_by_name['GetBinaryInfoResponse'] = _GETBINARYINFORESPONSE
DESCRIPTOR.message_types_by_name['GetChunkRequest'] = _GETCHUNKREQUEST
DESCRIPTOR.message_types_by_name['GetChunkResponse'] = _GETCHUNKRESPONSE
DESCRIPTOR.message_types_by_name['BinaryTransferError'] = _BINARYTRANSFERERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateBinaryRequest = _reflection.GeneratedProtocolMessageType('CreateBinaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBINARYREQUEST,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.CreateBinaryRequest)
  })
_sym_db.RegisterMessage(CreateBinaryRequest)

CreateBinaryResponse = _reflection.GeneratedProtocolMessageType('CreateBinaryResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBINARYRESPONSE,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.CreateBinaryResponse)
  })
_sym_db.RegisterMessage(CreateBinaryResponse)

UploadChunkRequest = _reflection.GeneratedProtocolMessageType('UploadChunkRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCHUNKREQUEST,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.UploadChunkRequest)
  })
_sym_db.RegisterMessage(UploadChunkRequest)

UploadChunkResponse = _reflection.GeneratedProtocolMessageType('UploadChunkResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCHUNKRESPONSE,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.UploadChunkResponse)
  })
_sym_db.RegisterMessage(UploadChunkResponse)

DeleteBinaryRequest = _reflection.GeneratedProtocolMessageType('DeleteBinaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBINARYREQUEST,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.DeleteBinaryRequest)
  })
_sym_db.RegisterMessage(DeleteBinaryRequest)

DeleteBinaryResponse = _reflection.GeneratedProtocolMessageType('DeleteBinaryResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBINARYRESPONSE,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.DeleteBinaryResponse)
  })
_sym_db.RegisterMessage(DeleteBinaryResponse)

GetBinaryInfoRequest = _reflection.GeneratedProtocolMessageType('GetBinaryInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBINARYINFOREQUEST,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.GetBinaryInfoRequest)
  })
_sym_db.RegisterMessage(GetBinaryInfoRequest)

GetBinaryInfoResponse = _reflection.GeneratedProtocolMessageType('GetBinaryInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBINARYINFORESPONSE,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.GetBinaryInfoResponse)
  })
_sym_db.RegisterMessage(GetBinaryInfoResponse)

GetChunkRequest = _reflection.GeneratedProtocolMessageType('GetChunkRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCHUNKREQUEST,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.GetChunkRequest)
  })
_sym_db.RegisterMessage(GetChunkRequest)

GetChunkResponse = _reflection.GeneratedProtocolMessageType('GetChunkResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCHUNKRESPONSE,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.GetChunkResponse)
  })
_sym_db.RegisterMessage(GetChunkResponse)

BinaryTransferError = _reflection.GeneratedProtocolMessageType('BinaryTransferError', (_message.Message,), {
  'DESCRIPTOR' : _BINARYTRANSFERERROR,
  '__module__' : 'SiLABinaryTransfer_pb2'
  # @@protoc_insertion_point(class_scope:sila2.org.silastandard.BinaryTransferError)
  })
_sym_db.RegisterMessage(BinaryTransferError)


DESCRIPTOR._options = None

_BINARYUPLOAD = _descriptor.ServiceDescriptor(
  name='BinaryUpload',
  full_name='sila2.org.silastandard.BinaryUpload',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1166,
  serialized_end=1508,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateBinary',
    full_name='sila2.org.silastandard.BinaryUpload.CreateBinary',
    index=0,
    containing_service=None,
    input_type=_CREATEBINARYREQUEST,
    output_type=_CREATEBINARYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UploadChunk',
    full_name='sila2.org.silastandard.BinaryUpload.UploadChunk',
    index=1,
    containing_service=None,
    input_type=_UPLOADCHUNKREQUEST,
    output_type=_UPLOADCHUNKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBinary',
    full_name='sila2.org.silastandard.BinaryUpload.DeleteBinary',
    index=2,
    containing_service=None,
    input_type=_DELETEBINARYREQUEST,
    output_type=_DELETEBINARYRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BINARYUPLOAD)

DESCRIPTOR.services_by_name['BinaryUpload'] = _BINARYUPLOAD


_BINARYDOWNLOAD = _descriptor.ServiceDescriptor(
  name='BinaryDownload',
  full_name='sila2.org.silastandard.BinaryDownload',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1511,
  serialized_end=1849,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBinaryInfo',
    full_name='sila2.org.silastandard.BinaryDownload.GetBinaryInfo',
    index=0,
    containing_service=None,
    input_type=_GETBINARYINFOREQUEST,
    output_type=_GETBINARYINFORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetChunk',
    full_name='sila2.org.silastandard.BinaryDownload.GetChunk',
    index=1,
    containing_service=None,
    input_type=_GETCHUNKREQUEST,
    output_type=_GETCHUNKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBinary',
    full_name='sila2.org.silastandard.BinaryDownload.DeleteBinary',
    index=2,
    containing_service=None,
    input_type=_DELETEBINARYREQUEST,
    output_type=_DELETEBINARYRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BINARYDOWNLOAD)

DESCRIPTOR.services_by_name['BinaryDownload'] = _BINARYDOWNLOAD

# @@protoc_insertion_point(module_scope)
