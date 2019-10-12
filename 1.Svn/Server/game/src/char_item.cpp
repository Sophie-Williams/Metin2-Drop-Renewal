// 1.) Find this:
bool CHARACTER::DropItem(TItemPos Cell, BYTE bCount)
{
	...
	...
}

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
bool CHARACTER::DestroyItem(TItemPos Cell)
{
	LPITEM item = NULL;
	
	if (!CanHandleItem())
	{
		if (NULL != DragonSoul_RefineWindow_GetOpener())
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("강화창을 연 상태에서는 아이템을 옮길 수 없습니다."));
		return false;
	}
	
	if (IsDead())
		return false;
	
	if (!IsValidItemPosition(Cell) || !(item = GetItem(Cell)))
		return false;
	
	if (item->IsExchanging())
		return false;
	
	if (true == item->isLocked())
		return false;
	
#ifdef ENABLE_SOULBINDING_SYSTEM
	if (item->IsBind() || item->IsUntilBind())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("BIND_ITEM_NOT_DELETE"));
		return false;
	}
#endif

	if (quest::CQuestManager::instance().GetPCForce(GetPlayerID())->IsRunning() == true)
		return false;
	
	if (item->GetCount() <= 0)
		return false;
	
#ifdef ENABLE_GROWTH_PET_SYSTEM
	if (item->GetVnum() == 55701 || item->GetVnum() == 55702 || item->GetVnum() == 55703 || item->GetVnum() == 55704)
		if (GetNewPetSystem()->IsActivePet())
			return false;
#endif

	SyncQuickslot(QUICKSLOT_TYPE_ITEM, Cell.cell, 1000);
	ITEM_MANAGER::instance().RemoveItem(item);
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ITEM_DESTROY_SUCCES"), item->GetName());
	return true;
}

bool CHARACTER::SellItem(TItemPos Cell, BYTE bCount)
{
	LPITEM item = NULL;
	
	if (!CanHandleItem())
	{
		if (NULL != DragonSoul_RefineWindow_GetOpener())
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("강화창을 연 상태에서는 아이템을 옮길 수 없습니다."));
		return false;
	}
	
	if (IsDead())
		return false;
	
	if (!IsValidItemPosition(Cell) || !(item = GetItem(Cell)))
		return false;
	
	if (item->IsExchanging())
		return false;
	
	if (true == item->isLocked())
		return false;
	
#ifdef ENABLE_SOULBINDING_SYSTEM
	if (item->IsBind() || item->IsUntilBind())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("BIND_ITEM_NOT_SELL"));
		return false;
	}
#endif

	if (IS_SET(item->GetAntiFlag(), ITEM_ANTIFLAG_SELL))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("THIS_ITEM_NOT_SELL"));
		return false;
	}
	
	if (quest::CQuestManager::instance().GetPCForce(GetPlayerID())->IsRunning() == true)
		return false;
	
	if (item->GetCount() <= 0)
		return false;
	
#ifdef ENABLE_GROWTH_PET_SYSTEM
	if (item->GetVnum() == 55701 || item->GetVnum() == 55702 || item->GetVnum() == 55703 || item->GetVnum() == 55704)
		if (GetNewPetSystem()->IsActivePet())
			return false;
#endif

	DWORD dwPrice;
	
	if (bCount == 0 || bCount > item->GetCount())
		bCount = item->GetCount();
	
	dwPrice = item->GetShopBuyPrice();
	
	if (IS_SET(item->GetFlag(), ITEM_FLAG_COUNT_PER_1GOLD))
	{
		if (dwPrice == 0)
			dwPrice = bCount;
		else
			dwPrice = bCount / dwPrice;
	}
	else
		dwPrice *= bCount;
	
	dwPrice /= 5;
	
	DWORD dwTax = 0;
	dwPrice -= dwTax;

	const int64_t nTotalMoney = static_cast<int64_t>(GetGold()) + static_cast<int64_t>(dwPrice);
	if (GOLD_MAX <= nTotalMoney)
	{
		sys_err("[OVERFLOW_GOLD] id %u name %s gold %u", GetPlayerID(), GetName(), GetGold());
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("20억냥이 초과하여 물품을 팔수 없습니다."));
		return false;
	}
	
	sys_log(0, "SHOP: SELL: %s item name: %s(x%d):%u price: %u", GetName(), item->GetName(), bCount, item->GetID(), dwPrice);

	DBManager::instance().SendMoneyLog(MONEY_LOG_SHOP, item->GetVnum(), dwPrice);
	item->SetCount(item->GetCount() - bCount);
	PointChange(POINT_GOLD, dwPrice, false);
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ITEM_SELL_SUCCES"), item->GetName());
	return true;
}
#endif

