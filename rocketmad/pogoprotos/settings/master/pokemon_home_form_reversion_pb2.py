# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/pokemon_home_form_reversion.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.enums import form_pb2 as pogoprotos_dot_enums_dot_form__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/pokemon_home_form_reversion.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n<pogoprotos/settings/master/pokemon_home_form_reversion.proto\x12\x1apogoprotos.settings.master\x1a!pogoprotos/enums/pokemon_id.proto\x1a\x1bpogoprotos/enums/form.proto\"\xb4\x02\n\x18PokemonHomeFormReversion\x12/\n\npokemon_id\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12V\n\x0c\x66orm_mapping\x18\x02 \x03(\x0b\x32@.pogoprotos.settings.master.PokemonHomeFormReversion.FormMapping\x1a\x8e\x01\n\x0b\x46ormMapping\x12-\n\rreverted_form\x18\x01 \x01(\x0e\x32\x16.pogoprotos.enums.Form\x12\x32\n\x12unauthorized_forms\x18\x02 \x03(\x0e\x32\x16.pogoprotos.enums.Form\x12\x1c\n\x14reverted_form_string\x18\x03 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_form__pb2.DESCRIPTOR,])




_POKEMONHOMEFORMREVERSION_FORMMAPPING = _descriptor.Descriptor(
  name='FormMapping',
  full_name='pogoprotos.settings.master.PokemonHomeFormReversion.FormMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reverted_form', full_name='pogoprotos.settings.master.PokemonHomeFormReversion.FormMapping.reverted_form', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unauthorized_forms', full_name='pogoprotos.settings.master.PokemonHomeFormReversion.FormMapping.unauthorized_forms', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reverted_form_string', full_name='pogoprotos.settings.master.PokemonHomeFormReversion.FormMapping.reverted_form_string', index=2,
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
  serialized_start=323,
  serialized_end=465,
)

_POKEMONHOMEFORMREVERSION = _descriptor.Descriptor(
  name='PokemonHomeFormReversion',
  full_name='pogoprotos.settings.master.PokemonHomeFormReversion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.settings.master.PokemonHomeFormReversion.pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='form_mapping', full_name='pogoprotos.settings.master.PokemonHomeFormReversion.form_mapping', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POKEMONHOMEFORMREVERSION_FORMMAPPING, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=465,
)

_POKEMONHOMEFORMREVERSION_FORMMAPPING.fields_by_name['reverted_form'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
_POKEMONHOMEFORMREVERSION_FORMMAPPING.fields_by_name['unauthorized_forms'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
_POKEMONHOMEFORMREVERSION_FORMMAPPING.containing_type = _POKEMONHOMEFORMREVERSION
_POKEMONHOMEFORMREVERSION.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_POKEMONHOMEFORMREVERSION.fields_by_name['form_mapping'].message_type = _POKEMONHOMEFORMREVERSION_FORMMAPPING
DESCRIPTOR.message_types_by_name['PokemonHomeFormReversion'] = _POKEMONHOMEFORMREVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonHomeFormReversion = _reflection.GeneratedProtocolMessageType('PokemonHomeFormReversion', (_message.Message,), dict(

  FormMapping = _reflection.GeneratedProtocolMessageType('FormMapping', (_message.Message,), dict(
    DESCRIPTOR = _POKEMONHOMEFORMREVERSION_FORMMAPPING,
    __module__ = 'pogoprotos.settings.master.pokemon_home_form_reversion_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.PokemonHomeFormReversion.FormMapping)
    ))
  ,
  DESCRIPTOR = _POKEMONHOMEFORMREVERSION,
  __module__ = 'pogoprotos.settings.master.pokemon_home_form_reversion_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.PokemonHomeFormReversion)
  ))
_sym_db.RegisterMessage(PokemonHomeFormReversion)
_sym_db.RegisterMessage(PokemonHomeFormReversion.FormMapping)


# @@protoc_insertion_point(module_scope)