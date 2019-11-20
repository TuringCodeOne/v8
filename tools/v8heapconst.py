# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  64: "SYMBOL_TYPE",
  65: "BIG_INT_BASE_TYPE",
  66: "HEAP_NUMBER_TYPE",
  67: "ODDBALL_TYPE",
  68: "SOURCE_TEXT_MODULE_TYPE",
  69: "SYNTHETIC_MODULE_TYPE",
  70: "FOREIGN_TYPE",
  71: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  72: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  73: "CALLABLE_TASK_TYPE",
  74: "CALLBACK_TASK_TYPE",
  75: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  76: "LOAD_HANDLER_TYPE",
  77: "STORE_HANDLER_TYPE",
  78: "FUNCTION_TEMPLATE_INFO_TYPE",
  79: "OBJECT_TEMPLATE_INFO_TYPE",
  80: "ACCESS_CHECK_INFO_TYPE",
  81: "ACCESSOR_INFO_TYPE",
  82: "ACCESSOR_PAIR_TYPE",
  83: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  84: "ALLOCATION_MEMENTO_TYPE",
  85: "ALLOCATION_SITE_TYPE",
  86: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  87: "ASM_WASM_DATA_TYPE",
  88: "ASYNC_GENERATOR_REQUEST_TYPE",
  89: "CALL_HANDLER_INFO_TYPE",
  90: "CLASS_POSITIONS_TYPE",
  91: "DEBUG_INFO_TYPE",
  92: "ENUM_CACHE_TYPE",
  93: "FEEDBACK_CELL_TYPE",
  94: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  95: "INTERCEPTOR_INFO_TYPE",
  96: "INTERNAL_CLASS_TYPE",
  97: "INTERPRETER_DATA_TYPE",
  98: "PROMISE_CAPABILITY_TYPE",
  99: "PROMISE_REACTION_TYPE",
  100: "PROTOTYPE_INFO_TYPE",
  101: "SCRIPT_TYPE",
  102: "SMI_BOX_TYPE",
  103: "SMI_PAIR_TYPE",
  104: "SORT_STATE_TYPE",
  105: "SOURCE_POSITION_TABLE_WITH_FRAME_CACHE_TYPE",
  106: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  107: "STACK_FRAME_INFO_TYPE",
  108: "STACK_TRACE_FRAME_TYPE",
  109: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  110: "TUPLE2_TYPE",
  111: "TUPLE3_TYPE",
  112: "WASM_CAPI_FUNCTION_DATA_TYPE",
  113: "WASM_DEBUG_INFO_TYPE",
  114: "WASM_EXCEPTION_TAG_TYPE",
  115: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  116: "WASM_INDIRECT_FUNCTION_TABLE_TYPE",
  117: "WASM_JS_FUNCTION_DATA_TYPE",
  118: "FIXED_ARRAY_TYPE",
  119: "HASH_TABLE_TYPE",
  120: "EPHEMERON_HASH_TABLE_TYPE",
  121: "GLOBAL_DICTIONARY_TYPE",
  122: "NAME_DICTIONARY_TYPE",
  123: "NUMBER_DICTIONARY_TYPE",
  124: "ORDERED_HASH_MAP_TYPE",
  125: "ORDERED_HASH_SET_TYPE",
  126: "ORDERED_NAME_DICTIONARY_TYPE",
  127: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  128: "STRING_TABLE_TYPE",
  129: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  130: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  131: "SCOPE_INFO_TYPE",
  132: "SCRIPT_CONTEXT_TABLE_TYPE",
  133: "BYTE_ARRAY_TYPE",
  134: "BYTECODE_ARRAY_TYPE",
  135: "FIXED_DOUBLE_ARRAY_TYPE",
  136: "AWAIT_CONTEXT_TYPE",
  137: "BLOCK_CONTEXT_TYPE",
  138: "CATCH_CONTEXT_TYPE",
  139: "DEBUG_EVALUATE_CONTEXT_TYPE",
  140: "EVAL_CONTEXT_TYPE",
  141: "FUNCTION_CONTEXT_TYPE",
  142: "MODULE_CONTEXT_TYPE",
  143: "NATIVE_CONTEXT_TYPE",
  144: "SCRIPT_CONTEXT_TYPE",
  145: "WITH_CONTEXT_TYPE",
  146: "SMALL_ORDERED_HASH_MAP_TYPE",
  147: "SMALL_ORDERED_HASH_SET_TYPE",
  148: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  149: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  150: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  151: "WEAK_FIXED_ARRAY_TYPE",
  152: "TRANSITION_ARRAY_TYPE",
  153: "CELL_TYPE",
  154: "CODE_TYPE",
  155: "CODE_DATA_CONTAINER_TYPE",
  156: "DESCRIPTOR_ARRAY_TYPE",
  157: "EMBEDDER_DATA_ARRAY_TYPE",
  158: "FEEDBACK_METADATA_TYPE",
  159: "FEEDBACK_VECTOR_TYPE",
  160: "FILLER_TYPE",
  161: "FREE_SPACE_TYPE",
  162: "MAP_TYPE",
  163: "PREPARSE_DATA_TYPE",
  164: "PROPERTY_ARRAY_TYPE",
  165: "PROPERTY_CELL_TYPE",
  166: "SHARED_FUNCTION_INFO_TYPE",
  167: "WEAK_ARRAY_LIST_TYPE",
  168: "WEAK_CELL_TYPE",
  169: "JS_PROXY_TYPE",
  1057: "JS_OBJECT_TYPE",
  170: "JS_GLOBAL_OBJECT_TYPE",
  171: "JS_GLOBAL_PROXY_TYPE",
  172: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1042: "JS_MAP_KEY_ITERATOR_TYPE",
  1043: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1044: "JS_MAP_VALUE_ITERATOR_TYPE",
  1045: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1046: "JS_SET_VALUE_ITERATOR_TYPE",
  1047: "JS_GENERATOR_OBJECT_TYPE",
  1048: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1049: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1050: "JS_DATA_VIEW_TYPE",
  1051: "JS_TYPED_ARRAY_TYPE",
  1052: "JS_MAP_TYPE",
  1053: "JS_SET_TYPE",
  1054: "JS_WEAK_MAP_TYPE",
  1055: "JS_WEAK_SET_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_OBJECT_TYPE",
  1059: "JS_ARRAY_TYPE",
  1060: "JS_ARRAY_BUFFER_TYPE",
  1061: "JS_ARRAY_ITERATOR_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_COLLATOR_TYPE",
  1064: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1065: "JS_DATE_TYPE",
  1066: "JS_DATE_TIME_FORMAT_TYPE",
  1067: "JS_DISPLAY_NAMES_TYPE",
  1068: "JS_ERROR_TYPE",
  1069: "JS_FINALIZATION_GROUP_TYPE",
  1070: "JS_FINALIZATION_GROUP_CLEANUP_ITERATOR_TYPE",
  1071: "JS_LIST_FORMAT_TYPE",
  1072: "JS_LOCALE_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_NUMBER_FORMAT_TYPE",
  1075: "JS_PLURAL_RULES_TYPE",
  1076: "JS_PROMISE_TYPE",
  1077: "JS_REG_EXP_TYPE",
  1078: "JS_REG_EXP_STRING_ITERATOR_TYPE",
  1079: "JS_RELATIVE_TIME_FORMAT_TYPE",
  1080: "JS_SEGMENT_ITERATOR_TYPE",
  1081: "JS_SEGMENTER_TYPE",
  1082: "JS_STRING_ITERATOR_TYPE",
  1083: "JS_V8_BREAK_ITERATOR_TYPE",
  1084: "JS_WEAK_REF_TYPE",
  1085: "WASM_EXCEPTION_OBJECT_TYPE",
  1086: "WASM_GLOBAL_OBJECT_TYPE",
  1087: "WASM_INSTANCE_OBJECT_TYPE",
  1088: "WASM_MEMORY_OBJECT_TYPE",
  1089: "WASM_MODULE_OBJECT_TYPE",
  1090: "WASM_TABLE_OBJECT_TYPE",
  1091: "JS_BOUND_FUNCTION_TYPE",
  1092: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x00119): (161, "FreeSpaceMap"),
  ("read_only_space", 0x00161): (162, "MetaMap"),
  ("read_only_space", 0x001d9): (67, "NullMap"),
  ("read_only_space", 0x00239): (156, "DescriptorArrayMap"),
  ("read_only_space", 0x00291): (151, "WeakFixedArrayMap"),
  ("read_only_space", 0x002d9): (160, "OnePointerFillerMap"),
  ("read_only_space", 0x00321): (160, "TwoPointerFillerMap"),
  ("read_only_space", 0x00399): (67, "UninitializedMap"),
  ("read_only_space", 0x00401): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x00499): (67, "UndefinedMap"),
  ("read_only_space", 0x004f1): (66, "HeapNumberMap"),
  ("read_only_space", 0x00569): (67, "TheHoleMap"),
  ("read_only_space", 0x00609): (67, "BooleanMap"),
  ("read_only_space", 0x006d9): (133, "ByteArrayMap"),
  ("read_only_space", 0x00721): (118, "FixedArrayMap"),
  ("read_only_space", 0x00769): (118, "FixedCOWArrayMap"),
  ("read_only_space", 0x007b1): (119, "HashTableMap"),
  ("read_only_space", 0x007f9): (64, "SymbolMap"),
  ("read_only_space", 0x00841): (40, "OneByteStringMap"),
  ("read_only_space", 0x00889): (131, "ScopeInfoMap"),
  ("read_only_space", 0x008d1): (166, "SharedFunctionInfoMap"),
  ("read_only_space", 0x00919): (154, "CodeMap"),
  ("read_only_space", 0x00961): (153, "CellMap"),
  ("read_only_space", 0x009a9): (165, "GlobalPropertyCellMap"),
  ("read_only_space", 0x009f1): (70, "ForeignMap"),
  ("read_only_space", 0x00a39): (152, "TransitionArrayMap"),
  ("read_only_space", 0x00a81): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x00ac9): (159, "FeedbackVectorMap"),
  ("read_only_space", 0x00b61): (67, "ArgumentsMarkerMap"),
  ("read_only_space", 0x00bf9): (67, "ExceptionMap"),
  ("read_only_space", 0x00c91): (67, "TerminationExceptionMap"),
  ("read_only_space", 0x00d31): (67, "OptimizedOutMap"),
  ("read_only_space", 0x00dc9): (67, "StaleRegisterMap"),
  ("read_only_space", 0x00e31): (132, "ScriptContextTableMap"),
  ("read_only_space", 0x00e79): (129, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x00ec1): (158, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x00f09): (118, "ArrayListMap"),
  ("read_only_space", 0x00f51): (65, "BigIntMap"),
  ("read_only_space", 0x00f99): (130, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x00fe1): (134, "BytecodeArrayMap"),
  ("read_only_space", 0x01029): (155, "CodeDataContainerMap"),
  ("read_only_space", 0x01071): (135, "FixedDoubleArrayMap"),
  ("read_only_space", 0x010b9): (121, "GlobalDictionaryMap"),
  ("read_only_space", 0x01101): (93, "ManyClosuresCellMap"),
  ("read_only_space", 0x01149): (118, "ModuleInfoMap"),
  ("read_only_space", 0x01191): (122, "NameDictionaryMap"),
  ("read_only_space", 0x011d9): (93, "NoClosuresCellMap"),
  ("read_only_space", 0x01221): (123, "NumberDictionaryMap"),
  ("read_only_space", 0x01269): (93, "OneClosureCellMap"),
  ("read_only_space", 0x012b1): (124, "OrderedHashMapMap"),
  ("read_only_space", 0x012f9): (125, "OrderedHashSetMap"),
  ("read_only_space", 0x01341): (126, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x01389): (163, "PreparseDataMap"),
  ("read_only_space", 0x013d1): (164, "PropertyArrayMap"),
  ("read_only_space", 0x01419): (89, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x01461): (89, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x014a9): (89, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x014f1): (127, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x01539): (118, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x01581): (146, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x015c9): (147, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x01611): (148, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x01659): (68, "SourceTextModuleMap"),
  ("read_only_space", 0x016a1): (128, "StringTableMap"),
  ("read_only_space", 0x016e9): (69, "SyntheticModuleMap"),
  ("read_only_space", 0x01731): (150, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x01779): (149, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x017c1): (167, "WeakArrayListMap"),
  ("read_only_space", 0x01809): (120, "EphemeronHashTableMap"),
  ("read_only_space", 0x01851): (157, "EmbedderDataArrayMap"),
  ("read_only_space", 0x01899): (168, "WeakCellMap"),
  ("read_only_space", 0x018e1): (32, "StringMap"),
  ("read_only_space", 0x01929): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x01971): (33, "ConsStringMap"),
  ("read_only_space", 0x019b9): (37, "ThinStringMap"),
  ("read_only_space", 0x01a01): (35, "SlicedStringMap"),
  ("read_only_space", 0x01a49): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x01a91): (34, "ExternalStringMap"),
  ("read_only_space", 0x01ad9): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x01b21): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x01b69): (0, "InternalizedStringMap"),
  ("read_only_space", 0x01bb1): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x01bf9): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x01c41): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x01c89): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x01cd1): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x01d19): (67, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x01d79): (92, "EnumCacheMap"),
  ("read_only_space", 0x01e11): (86, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x01ff9): (95, "InterceptorInfoMap"),
  ("read_only_space", 0x049d1): (71, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x04a19): (72, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x04a61): (73, "CallableTaskMap"),
  ("read_only_space", 0x04aa9): (74, "CallbackTaskMap"),
  ("read_only_space", 0x04af1): (75, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x04b39): (78, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x04b81): (79, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x04bc9): (80, "AccessCheckInfoMap"),
  ("read_only_space", 0x04c11): (81, "AccessorInfoMap"),
  ("read_only_space", 0x04c59): (82, "AccessorPairMap"),
  ("read_only_space", 0x04ca1): (83, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x04ce9): (84, "AllocationMementoMap"),
  ("read_only_space", 0x04d31): (87, "AsmWasmDataMap"),
  ("read_only_space", 0x04d79): (88, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x04dc1): (90, "ClassPositionsMap"),
  ("read_only_space", 0x04e09): (91, "DebugInfoMap"),
  ("read_only_space", 0x04e51): (94, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x04e99): (97, "InterpreterDataMap"),
  ("read_only_space", 0x04ee1): (98, "PromiseCapabilityMap"),
  ("read_only_space", 0x04f29): (99, "PromiseReactionMap"),
  ("read_only_space", 0x04f71): (100, "PrototypeInfoMap"),
  ("read_only_space", 0x04fb9): (101, "ScriptMap"),
  ("read_only_space", 0x05001): (105, "SourcePositionTableWithFrameCacheMap"),
  ("read_only_space", 0x05049): (106, "SourceTextModuleInfoEntryMap"),
  ("read_only_space", 0x05091): (107, "StackFrameInfoMap"),
  ("read_only_space", 0x050d9): (108, "StackTraceFrameMap"),
  ("read_only_space", 0x05121): (109, "TemplateObjectDescriptionMap"),
  ("read_only_space", 0x05169): (110, "Tuple2Map"),
  ("read_only_space", 0x051b1): (111, "Tuple3Map"),
  ("read_only_space", 0x051f9): (112, "WasmCapiFunctionDataMap"),
  ("read_only_space", 0x05241): (113, "WasmDebugInfoMap"),
  ("read_only_space", 0x05289): (114, "WasmExceptionTagMap"),
  ("read_only_space", 0x052d1): (115, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x05319): (116, "WasmIndirectFunctionTableMap"),
  ("read_only_space", 0x05361): (117, "WasmJSFunctionDataMap"),
  ("read_only_space", 0x053a9): (96, "InternalClassMap"),
  ("read_only_space", 0x053f1): (103, "SmiPairMap"),
  ("read_only_space", 0x05439): (102, "SmiBoxMap"),
  ("read_only_space", 0x05481): (104, "SortStateMap"),
  ("read_only_space", 0x054c9): (85, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x05511): (85, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x05559): (76, "LoadHandler1Map"),
  ("read_only_space", 0x055a1): (76, "LoadHandler2Map"),
  ("read_only_space", 0x055e9): (76, "LoadHandler3Map"),
  ("read_only_space", 0x05631): (77, "StoreHandler0Map"),
  ("read_only_space", 0x05679): (77, "StoreHandler1Map"),
  ("read_only_space", 0x056c1): (77, "StoreHandler2Map"),
  ("read_only_space", 0x05709): (77, "StoreHandler3Map"),
  ("map_space", 0x00119): (1057, "ExternalMap"),
  ("map_space", 0x00161): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x001a9): "NullValue",
  ("read_only_space", 0x00221): "EmptyDescriptorArray",
  ("read_only_space", 0x00281): "EmptyWeakFixedArray",
  ("read_only_space", 0x00369): "UninitializedValue",
  ("read_only_space", 0x00469): "UndefinedValue",
  ("read_only_space", 0x004e1): "NanValue",
  ("read_only_space", 0x00539): "TheHoleValue",
  ("read_only_space", 0x005c9): "HoleNanValue",
  ("read_only_space", 0x005d9): "TrueValue",
  ("read_only_space", 0x00681): "FalseValue",
  ("read_only_space", 0x006c9): "empty_string",
  ("read_only_space", 0x00b11): "EmptyScopeInfo",
  ("read_only_space", 0x00b21): "EmptyFixedArray",
  ("read_only_space", 0x00b31): "ArgumentsMarker",
  ("read_only_space", 0x00bc9): "Exception",
  ("read_only_space", 0x00c61): "TerminationException",
  ("read_only_space", 0x00d01): "OptimizedOut",
  ("read_only_space", 0x00d99): "StaleRegister",
  ("read_only_space", 0x01d61): "EmptyEnumCache",
  ("read_only_space", 0x01dc1): "EmptyPropertyArray",
  ("read_only_space", 0x01dd1): "EmptyByteArray",
  ("read_only_space", 0x01de1): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x01df9): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x01e59): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x01e69): "EmptySloppyArgumentsElements",
  ("read_only_space", 0x01e89): "EmptySlowElementDictionary",
  ("read_only_space", 0x01ed1): "EmptyOrderedHashMap",
  ("read_only_space", 0x01ef9): "EmptyOrderedHashSet",
  ("read_only_space", 0x01f21): "EmptyFeedbackMetadata",
  ("read_only_space", 0x01f31): "EmptyPropertyCell",
  ("read_only_space", 0x01f59): "EmptyPropertyDictionary",
  ("read_only_space", 0x01fa9): "NoOpInterceptorInfo",
  ("read_only_space", 0x02041): "EmptyWeakArrayList",
  ("read_only_space", 0x02059): "InfinityValue",
  ("read_only_space", 0x02069): "MinusZeroValue",
  ("read_only_space", 0x02079): "MinusInfinityValue",
  ("read_only_space", 0x02089): "SelfReferenceMarker",
  ("read_only_space", 0x020e1): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x020f9): "TrampolineTrivialCodeDataContainer",
  ("read_only_space", 0x02111): "TrampolinePromiseRejectionCodeDataContainer",
  ("read_only_space", 0x02129): "GlobalThisBindingScopeInfo",
  ("read_only_space", 0x02191): "EmptyFunctionScopeInfo",
  ("read_only_space", 0x021e1): "NativeScopeInfo",
  ("read_only_space", 0x02219): "HashSeed",
  ("old_space", 0x00119): "ArgumentsIteratorAccessor",
  ("old_space", 0x00189): "ArrayLengthAccessor",
  ("old_space", 0x001f9): "BoundFunctionLengthAccessor",
  ("old_space", 0x00269): "BoundFunctionNameAccessor",
  ("old_space", 0x002d9): "ErrorStackAccessor",
  ("old_space", 0x00349): "FunctionArgumentsAccessor",
  ("old_space", 0x003b9): "FunctionCallerAccessor",
  ("old_space", 0x00429): "FunctionNameAccessor",
  ("old_space", 0x00499): "FunctionLengthAccessor",
  ("old_space", 0x00509): "FunctionPrototypeAccessor",
  ("old_space", 0x00579): "RegExpResultIndicesAccessor",
  ("old_space", 0x005e9): "StringLengthAccessor",
  ("old_space", 0x00659): "InvalidPrototypeValidityCell",
  ("old_space", 0x00669): "EmptyScript",
  ("old_space", 0x006e9): "ManyClosuresCell",
  ("old_space", 0x00701): "ArrayConstructorProtector",
  ("old_space", 0x00729): "NoElementsProtector",
  ("old_space", 0x00751): "IsConcatSpreadableProtector",
  ("old_space", 0x00779): "ArraySpeciesProtector",
  ("old_space", 0x007a1): "TypedArraySpeciesProtector",
  ("old_space", 0x007c9): "PromiseSpeciesProtector",
  ("old_space", 0x007f1): "StringLengthProtector",
  ("old_space", 0x00819): "ArrayIteratorProtector",
  ("old_space", 0x00841): "ArrayBufferDetachingProtector",
  ("old_space", 0x00869): "PromiseHookProtector",
  ("old_space", 0x00891): "PromiseResolveProtector",
  ("old_space", 0x008b9): "MapIteratorProtector",
  ("old_space", 0x008e1): "PromiseThenProtector",
  ("old_space", 0x00909): "SetIteratorProtector",
  ("old_space", 0x00931): "StringIteratorProtector",
  ("old_space", 0x00959): "SingleCharacterStringCache",
  ("old_space", 0x01169): "StringSplitCache",
  ("old_space", 0x01979): "RegExpMultipleCache",
  ("old_space", 0x02189): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.