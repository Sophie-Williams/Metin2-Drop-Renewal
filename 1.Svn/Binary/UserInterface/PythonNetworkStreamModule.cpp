// 1.) Find this:
PyObject* netSendItemDropPacketNew(PyObject* poSelf, PyObject* poArgs)
{
	...
	...
}

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
PyObject* netSendItemDestroyPacket(PyObject* poSelf, PyObject* poArgs)
{
	TItemPos Cell;

	if (!PyTuple_GetInteger(poArgs, 0, &Cell.cell))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
	rkNetStream.SendItemDestroyPacket(Cell);

	return Py_BuildNone();
}

PyObject* netSendItemSellPacket(PyObject* poSelf, PyObject* poArgs)
{
	TItemPos Cell;

	if (!PyTuple_GetInteger(poArgs, 0, &Cell.cell))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
	rkNetStream.SendItemSellPacket(Cell);

	return Py_BuildNone();
}
#endif

// 1.) Find this:
		{ "SendItemDropPacketNew",				netSendItemDropPacketNew,				METH_VARARGS },

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
		{ "SendItemDestroyPacket",				netSendItemDestroyPacket,				METH_VARARGS },
		{ "SendItemSellPacket",					netSendItemSellPacket,					METH_VARARGS },
#endif
