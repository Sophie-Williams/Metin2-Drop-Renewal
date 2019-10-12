// 1.) Find this:
	HEADER_CG_ITEM_DROP2			= 20,

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
	HEADER_CG_ITEM_DESTROY			= 21,
	HEADER_CG_ITEM_SELL				= 22,
#endif

// 1.) Find this:
typedef struct command_item_drop2
{
	BYTE 	header;
	TItemPos 	Cell;
	DWORD	gold;
	BYTE	count;
} TPacketCGItemDrop2;

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
typedef struct command_item_destroy
{
	BYTE		header;
	TItemPos	Cell;
} TPacketCGItemDestroy;

typedef struct command_item_sell
{
	BYTE		header;
	TItemPos	Cell;
} TPacketCGItemSell;
#endif