# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tachi_classes.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13tachi_classes.proto\"\x97\x02\n\x06\x42\x61\x63kup\x12!\n\x0b\x62\x61\x63kupManga\x18\x01 \x03(\x0b\x32\x0c.BackupManga\x12)\n\x10\x62\x61\x63kupCategories\x18\x02 \x03(\x0b\x32\x0f.BackupCategory\x12\x30\n\x13\x62\x61\x63kupBrokenSources\x18\x64 \x03(\x0b\x32\x13.BrokenBackupSource\x12$\n\rbackupSources\x18\x65 \x03(\x0b\x32\r.BackupSource\x12,\n\x11\x62\x61\x63kupPreferences\x18h \x03(\x0b\x32\x11.BackupPreference\x12\x39\n\x17\x62\x61\x63kupSourcePreferences\x18i \x03(\x0b\x32\x18.BackupSourcePreferences\"\xde\x05\n\x0b\x42\x61\x63kupManga\x12\x0e\n\x06source\x18\x01 \x01(\x03\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x04 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\r\n\x05genre\x18\x07 \x03(\t\x12\x0e\n\x06status\x18\x08 \x01(\x05\x12\x14\n\x0cthumbnailUrl\x18\t \x01(\t\x12\x11\n\tdateAdded\x18\r \x01(\x03\x12\x0e\n\x06viewer\x18\x0e \x01(\x05\x12 \n\x08\x63hapters\x18\x10 \x03(\x0b\x32\x0e.BackupChapter\x12\x12\n\ncategories\x18\x11 \x03(\x03\x12!\n\x08tracking\x18\x12 \x03(\x0b\x32\x0f.BackupTracking\x12\x10\n\x08\x66\x61vorite\x18\x64 \x01(\x08\x12\x14\n\x0c\x63hapterFlags\x18\x65 \x01(\x05\x12+\n\rbrokenHistory\x18\x66 \x03(\x0b\x32\x14.BrokenBackupHistory\x12\x14\n\x0cviewer_flags\x18g \x01(\x05\x12\x1f\n\x07history\x18h \x03(\x0b\x32\x0e.BackupHistory\x12\x16\n\x0eupdateStrategy\x18i \x01(\x05\x12\x16\n\x0elastModifiedAt\x18j \x01(\x03\x12\x1a\n\x12\x66\x61voriteModifiedAt\x18k \x01(\x03\x12\x19\n\x0b\x63ustomTitle\x18\xa0\x06 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\x0c\x63ustomArtist\x18\xa1\x06 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\x0c\x63ustomAuthor\x18\xa2\x06 \x01(\tH\x02\x88\x01\x01\x12\x1f\n\x11\x63ustomDescription\x18\xa4\x06 \x01(\tH\x03\x88\x01\x01\x12\x19\n\x0b\x63ustomGenre\x18\xa5\x06 \x01(\tH\x04\x88\x01\x01\x42\x0e\n\x0c_customTitleB\x0f\n\r_customArtistB\x0f\n\r_customAuthorB\x14\n\x12_customDescriptionB\x0e\n\x0c_customGenre\"\xde\x01\n\rBackupChapter\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tscanlator\x18\x03 \x01(\t\x12\x0c\n\x04read\x18\x04 \x01(\x08\x12\x10\n\x08\x62ookmark\x18\x05 \x01(\x08\x12\x14\n\x0clastPageRead\x18\x06 \x01(\x03\x12\x11\n\tdateFetch\x18\x07 \x01(\x03\x12\x12\n\ndateUpload\x18\x08 \x01(\x03\x12\x15\n\rchapterNumber\x18\t \x01(\x02\x12\x13\n\x0bsourceOrder\x18\n \x01(\x03\x12\x16\n\x0elastModifiedAt\x18\x0b \x01(\x03\"<\n\x0e\x42\x61\x63kupCategory\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05order\x18\x02 \x01(\x03\x12\r\n\x05\x66lags\x18\x64 \x01(\x03\"\x84\x02\n\x0e\x42\x61\x63kupTracking\x12\x0e\n\x06syncId\x18\x01 \x01(\x05\x12\x11\n\tlibraryId\x18\x02 \x01(\x03\x12\x12\n\nmediaIdInt\x18\x03 \x01(\x05\x12\x13\n\x0btrackingUrl\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x17\n\x0flastChapterRead\x18\x06 \x01(\x02\x12\x15\n\rtotalChapters\x18\x07 \x01(\x05\x12\r\n\x05score\x18\x08 \x01(\x02\x12\x0e\n\x06status\x18\t \x01(\x05\x12\x1a\n\x12startedReadingDate\x18\n \x01(\x03\x12\x1b\n\x13\x66inishedReadingDate\x18\x0b \x01(\x03\x12\x0f\n\x07mediaId\x18\x64 \x01(\x03\"D\n\rBackupHistory\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08lastRead\x18\x02 \x01(\x03\x12\x14\n\x0creadDuration\x18\x03 \x01(\x03\"J\n\x13\x42rokenBackupHistory\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08lastRead\x18\x02 \x01(\x03\x12\x14\n\x0creadDuration\x18\x03 \x01(\x03\".\n\x0c\x42\x61\x63kupSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08sourceId\x18\x02 \x01(\x03\"4\n\x12\x42rokenBackupSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08sourceId\x18\x02 \x01(\x03\"@\n\x10\x42\x61\x63kupPreference\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.PreferenceValue\"N\n\x17\x42\x61\x63kupSourcePreferences\x12\x11\n\tsourceKey\x18\x01 \x01(\t\x12 \n\x05prefs\x18\x02 \x03(\x0b\x32\x11.BackupPreference\"\xad\x02\n\x0fPreferenceValue\x12\'\n\x08intValue\x18\x01 \x01(\x0b\x32\x13.IntPreferenceValueH\x00\x12)\n\tlongValue\x18\x02 \x01(\x0b\x32\x14.LongPreferenceValueH\x00\x12+\n\nfloatValue\x18\x03 \x01(\x0b\x32\x15.FloatPreferenceValueH\x00\x12-\n\x0bstringValue\x18\x04 \x01(\x0b\x32\x16.StringPreferenceValueH\x00\x12,\n\tboolValue\x18\x05 \x01(\x0b\x32\x17.BooleanPreferenceValueH\x00\x12\x33\n\x0estringSetValue\x18\x06 \x01(\x0b\x32\x19.StringSetPreferenceValueH\x00\x42\x07\n\x05value\"#\n\x12IntPreferenceValue\x12\r\n\x05value\x18\x01 \x01(\x05\"$\n\x13LongPreferenceValue\x12\r\n\x05value\x18\x01 \x01(\x03\"%\n\x14\x46loatPreferenceValue\x12\r\n\x05value\x18\x01 \x01(\x02\"&\n\x15StringPreferenceValue\x12\r\n\x05value\x18\x01 \x01(\t\"\'\n\x16\x42ooleanPreferenceValue\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18StringSetPreferenceValue\x12\r\n\x05value\x18\x01 \x03(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tachi_classes_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BACKUP']._serialized_start=24
  _globals['_BACKUP']._serialized_end=303
  _globals['_BACKUPMANGA']._serialized_start=306
  _globals['_BACKUPMANGA']._serialized_end=1040
  _globals['_BACKUPCHAPTER']._serialized_start=1043
  _globals['_BACKUPCHAPTER']._serialized_end=1265
  _globals['_BACKUPCATEGORY']._serialized_start=1267
  _globals['_BACKUPCATEGORY']._serialized_end=1327
  _globals['_BACKUPTRACKING']._serialized_start=1330
  _globals['_BACKUPTRACKING']._serialized_end=1590
  _globals['_BACKUPHISTORY']._serialized_start=1592
  _globals['_BACKUPHISTORY']._serialized_end=1660
  _globals['_BROKENBACKUPHISTORY']._serialized_start=1662
  _globals['_BROKENBACKUPHISTORY']._serialized_end=1736
  _globals['_BACKUPSOURCE']._serialized_start=1738
  _globals['_BACKUPSOURCE']._serialized_end=1784
  _globals['_BROKENBACKUPSOURCE']._serialized_start=1786
  _globals['_BROKENBACKUPSOURCE']._serialized_end=1838
  _globals['_BACKUPPREFERENCE']._serialized_start=1840
  _globals['_BACKUPPREFERENCE']._serialized_end=1904
  _globals['_BACKUPSOURCEPREFERENCES']._serialized_start=1906
  _globals['_BACKUPSOURCEPREFERENCES']._serialized_end=1984
  _globals['_PREFERENCEVALUE']._serialized_start=1987
  _globals['_PREFERENCEVALUE']._serialized_end=2288
  _globals['_INTPREFERENCEVALUE']._serialized_start=2290
  _globals['_INTPREFERENCEVALUE']._serialized_end=2325
  _globals['_LONGPREFERENCEVALUE']._serialized_start=2327
  _globals['_LONGPREFERENCEVALUE']._serialized_end=2363
  _globals['_FLOATPREFERENCEVALUE']._serialized_start=2365
  _globals['_FLOATPREFERENCEVALUE']._serialized_end=2402
  _globals['_STRINGPREFERENCEVALUE']._serialized_start=2404
  _globals['_STRINGPREFERENCEVALUE']._serialized_end=2442
  _globals['_BOOLEANPREFERENCEVALUE']._serialized_start=2444
  _globals['_BOOLEANPREFERENCEVALUE']._serialized_end=2483
  _globals['_STRINGSETPREFERENCEVALUE']._serialized_start=2485
  _globals['_STRINGSETPREFERENCEVALUE']._serialized_end=2526
# @@protoc_insertion_point(module_scope)
