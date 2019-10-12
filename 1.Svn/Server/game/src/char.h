// 1.) Find this:
		bool			DropItem(TItemPos Cell,  BYTE bCount=0);

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
		bool			DestroyItem(TItemPos Cell);
		bool			SellItem(TItemPos Cell, BYTE bCount=0);
#endif