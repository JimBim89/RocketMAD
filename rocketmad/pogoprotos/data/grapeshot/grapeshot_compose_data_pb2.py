# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/grapeshot/grapeshot_compose_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.grapeshot import grapeshot_authentication_data_pb2 as pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__authentication__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/grapeshot/grapeshot_compose_data.proto',
  package='pogoprotos.data.grapeshot',
  syntax='proto3',
  serialized_pb=_b('\n6pogoprotos/data/grapeshot/grapeshot_compose_data.proto\x12\x19pogoprotos.data.grapeshot\x1a=pogoprotos/data/grapeshot/grapeshot_authentication_data.proto\"\x80\x01\n\x14GrapeshotComposeData\x12\x18\n\x10target_file_path\x18\x01 \x01(\t\x12N\n\x0e\x61uthentication\x18\x02 \x01(\x0b\x32\x36.pogoprotos.data.grapeshot.GrapeshotAuthenticationDatab\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__authentication__data__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GRAPESHOTCOMPOSEDATA = _descriptor.Descriptor(
  name='GrapeshotComposeData',
  full_name='pogoprotos.data.grapeshot.GrapeshotComposeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_file_path', full_name='pogoprotos.data.grapeshot.GrapeshotComposeData.target_file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authentication', full_name='pogoprotos.data.grapeshot.GrapeshotComposeData.authentication', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=277,
)

_GRAPESHOTCOMPOSEDATA.fields_by_name['authentication'].message_type = pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__authentication__data__pb2._GRAPESHOTAUTHENTICATIONDATA
DESCRIPTOR.message_types_by_name['GrapeshotComposeData'] = _GRAPESHOTCOMPOSEDATA

GrapeshotComposeData = _reflection.GeneratedProtocolMessageType('GrapeshotComposeData', (_message.Message,), dict(
  DESCRIPTOR = _GRAPESHOTCOMPOSEDATA,
  __module__ = 'pogoprotos.data.grapeshot.grapeshot_compose_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.grapeshot.GrapeshotComposeData)
  ))
_sym_db.RegisterMessage(GrapeshotComposeData)


# @@protoc_insertion_point(module_scope)