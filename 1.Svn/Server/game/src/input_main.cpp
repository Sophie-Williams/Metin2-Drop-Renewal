// 1.) Find this:
void CInputMain::ItemDrop2(LPCHARACTER ch, const char * data)
{
	....
	....
}

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
void CInputMain::ItemDestroy(LPCHARACTER ch, const char * data)
{
	struct command_item_destroy * pinfo = (struct command_item_destroy *) data;
	if (ch)
		ch->DestroyItem(pinfo->Cell);
}

void CInputMain::ItemSell(LPCHARACTER ch, const char * data)
{
	struct command_item_sell * pinfo = (struct command_item_sell *) data;
	if (ch)
		ch->SellItem(pinfo->Cell);
}
#endif

// 1.) Find this:
		case HEADER_CG_ITEM_DROP2:
			if (!ch->IsObserverMode())
				ItemDrop2(ch, c_pData);
			break;

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
		case HEADER_CG_ITEM_DESTROY:
			if (!ch->IsObserverMode())
				ItemDestroy(ch, c_pData);
			break;

		case HEADER_CG_ITEM_SELL:
			if (!ch->IsObserverMode())
				ItemSell(ch, c_pData);
			break;
#endif
