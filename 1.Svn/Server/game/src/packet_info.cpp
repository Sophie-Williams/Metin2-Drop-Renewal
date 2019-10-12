// 1.) Find this:
	Set(HEADER_CG_ITEM_DROP2, sizeof(TPacketCGItemDrop2), "ItemDrop2", true);

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
	Set(HEADER_CG_ITEM_DESTROY,	sizeof(TPacketCGItemDestroy),	"ItemDestroy",	true);
	Set(HEADER_CG_ITEM_SELL,	sizeof(TPacketCGItemSell),		"ItemSell",		true);
#endif