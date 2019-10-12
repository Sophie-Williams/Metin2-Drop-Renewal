// 1.) Find this:
		bool SendItemDropPacketNew(TItemPos pos, DWORD elk, DWORD count);

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
		bool SendItemDestroyPacket(TItemPos pos);
		bool SendItemSellPacket(TItemPos pos);
#endif