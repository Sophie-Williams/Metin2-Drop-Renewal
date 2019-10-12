## 1.) Find this:
		def __DropItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount):
			# PRIVATESHOP_DISABLE_ITEM_DROP - 개인상점 열고 있는 동안 아이템 버림 방지
			if uiPrivateShopBuilder.IsBuildingPrivateShop():			
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
				return
			# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
			
			if player.SLOT_TYPE_INVENTORY == attachedType and player.IsEquipmentSlot(attachedItemSlotPos):
				self.stream.popupWindow.Close()
				self.stream.popupWindow.Open(localeInfo.DROP_ITEM_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)
			else:
				if player.SLOT_TYPE_INVENTORY == attachedType:
					dropItemIndex = player.GetItemIndex(attachedItemSlotPos)

					item.SelectItem(dropItemIndex)
					dropItemName = item.GetItemName()
					dropItemType = item.GetItemType()
					dropItemSubType = item.GetItemSubType()

					## Question Text
					questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)
				
				elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
					dropItemIndex = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, attachedItemSlotPos)

					item.SelectItem(dropItemIndex)
					dropItemName = item.GetItemName()
					dropItemType = item.GetItemType()
					dropItemSubType = item.GetItemSubType()

					## Question Text
					questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)

					## Dialog
					itemDropQuestionDialog = uiCommon.QuestionDialog()
					itemDropQuestionDialog.SetText(questionText)
					itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.RequestDropItem(arg))
					itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.RequestDropItem(arg))
					itemDropQuestionDialog.Open()
					itemDropQuestionDialog.dropType = attachedType
					itemDropQuestionDialog.dropNumber = attachedItemSlotPos
					itemDropQuestionDialog.dropCount = attachedItemCount
					self.itemDropQuestionDialog = itemDropQuestionDialog

					constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
					
				## Dialog_Equipments
				if dropItemType in [1, 2] and dropItemSubType in range(7) or dropItemType == 28 and dropItemSubType in [0, 1]:
					itemDropQuestionDialog = uiCommon.EquipmentDropQuestion()
					itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.RequestDropItem(arg))
					itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.RequestDropItem(arg))
					itemDropQuestionDialog.dropType = attachedType
					itemDropQuestionDialog.dropNumber = attachedItemSlotPos
					itemDropQuestionDialog.dropCount = attachedItemCount
					itemDropQuestionDialog.Open(attachedItemSlotPos)
					self.itemDropQuestionDialog = itemDropQuestionDialog

				## Dialog_Items
				else:
					itemDropQuestionDialog = uiCommon.QuestionDialog()
					itemDropQuestionDialog.SetText(questionText)
					itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.RequestDropItem(arg))
					itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.RequestDropItem(arg))
					itemDropQuestionDialog.Open()
					itemDropQuestionDialog.dropType = attachedType
					itemDropQuestionDialog.dropNumber = attachedItemSlotPos
					itemDropQuestionDialog.dropCount = attachedItemCount
					self.itemDropQuestionDialog = itemDropQuestionDialog

					constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

## 2.) Replace with this:
	if app.ENABLE_DROP_RENEWAL:
		def __DropItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount):
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
				return

			if player.SLOT_TYPE_INVENTORY == attachedType and player.IsEquipmentSlot(attachedItemSlotPos):
				self.stream.popupWindow.Close()
				self.stream.popupWindow.Open(localeInfo.DROP_ITEM_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)

			else:
				if player.SLOT_TYPE_INVENTORY == attachedType:
				# if player.SLOT_TYPE_INVENTORY == attachedType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == attachedType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == attachedType:
					dropItemIndex = player.GetItemIndex(attachedItemSlotPos)

					item.SelectItem(dropItemIndex)
					dropItemName = item.GetItemName()

					## Dialog
					if app.ENABLE_DROP_RENEWAL:
						itemDropQuestionDialog = uiCommon.DropRenewalDialog()
					else:
						itemDropQuestionDialog = uiCommon.QuestionDialog()
					itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
					if app.ENABLE_DROP_RENEWAL:
						itemDropQuestionDialog.SetDestroyEvent(lambda arg=True: self.RequestDestroyItem(arg))
						itemDropQuestionDialog.SetSellEvent(lambda arg=True: self.RequestSellItem(arg))
						itemDropQuestionDialog.SetItemSlot(attachedItemSlotPos)
					itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
					itemDropQuestionDialog.Open()
					itemDropQuestionDialog.dropType = attachedType
					itemDropQuestionDialog.dropNumber = attachedItemSlotPos
					itemDropQuestionDialog.dropCount = attachedItemCount
					self.itemDropQuestionDialog = itemDropQuestionDialog

					constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

				elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
					dropItemIndex = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, attachedItemSlotPos)

					item.SelectItem(dropItemIndex)
					dropItemName = item.GetItemName()

					## Dialog
					if app.ENABLE_DROP_RENEWAL:
						itemDropQuestionDialog = uiCommon.DropRenewalDialog()
					else:
						itemDropQuestionDialog = uiCommon.QuestionDialog()
					itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
					if app.ENABLE_DROP_RENEWAL:
						itemDropQuestionDialog.SetDestroyEvent(lambda arg=True: self.RequestDestroyItem(arg))
						itemDropQuestionDialog.SetSellEvent(lambda arg=True: self.RequestSellItem(arg))
						itemDropQuestionDialog.SetItemSlot(attachedItemSlotPos)
					itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
					itemDropQuestionDialog.Open()
					itemDropQuestionDialog.dropType = attachedType
					itemDropQuestionDialog.dropNumber = attachedItemSlotPos
					itemDropQuestionDialog.dropCount = attachedItemCount
					self.itemDropQuestionDialog = itemDropQuestionDialog

					constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
	else:
		def __DropItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount):
			# PRIVATESHOP_DISABLE_ITEM_DROP - 개인상점 열고 있는 동안 아이템 버림 방지
			if uiPrivateShopBuilder.IsBuildingPrivateShop():			
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
				return
			# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
			
			if player.SLOT_TYPE_INVENTORY == attachedType and player.IsEquipmentSlot(attachedItemSlotPos):
				self.stream.popupWindow.Close()
				self.stream.popupWindow.Open(localeInfo.DROP_ITEM_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)
			else:
				if player.SLOT_TYPE_INVENTORY == attachedType:
					dropItemIndex = player.GetItemIndex(attachedItemSlotPos)

					item.SelectItem(dropItemIndex)
					dropItemName = item.GetItemName()
					dropItemType = item.GetItemType()
					dropItemSubType = item.GetItemSubType()

					## Question Text
					questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)
				
				elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
					dropItemIndex = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, attachedItemSlotPos)

					item.SelectItem(dropItemIndex)
					dropItemName = item.GetItemName()
					dropItemType = item.GetItemType()
					dropItemSubType = item.GetItemSubType()

					## Question Text
					questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)

					## Dialog
					itemDropQuestionDialog = uiCommon.QuestionDialog()
					itemDropQuestionDialog.SetText(questionText)
					itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.RequestDropItem(arg))
					itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.RequestDropItem(arg))
					itemDropQuestionDialog.Open()
					itemDropQuestionDialog.dropType = attachedType
					itemDropQuestionDialog.dropNumber = attachedItemSlotPos
					itemDropQuestionDialog.dropCount = attachedItemCount
					self.itemDropQuestionDialog = itemDropQuestionDialog

					constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
					
				## Dialog_Equipments
				if dropItemType in [1, 2] and dropItemSubType in range(7) or dropItemType == 28 and dropItemSubType in [0, 1]:
					itemDropQuestionDialog = uiCommon.EquipmentDropQuestion()
					itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.RequestDropItem(arg))
					itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.RequestDropItem(arg))
					itemDropQuestionDialog.dropType = attachedType
					itemDropQuestionDialog.dropNumber = attachedItemSlotPos
					itemDropQuestionDialog.dropCount = attachedItemCount
					itemDropQuestionDialog.Open(attachedItemSlotPos)
					self.itemDropQuestionDialog = itemDropQuestionDialog

				## Dialog_Items
				else:
					itemDropQuestionDialog = uiCommon.QuestionDialog()
					itemDropQuestionDialog.SetText(questionText)
					itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.RequestDropItem(arg))
					itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.RequestDropItem(arg))
					itemDropQuestionDialog.Open()
					itemDropQuestionDialog.dropType = attachedType
					itemDropQuestionDialog.dropNumber = attachedItemSlotPos
					itemDropQuestionDialog.dropCount = attachedItemCount
					self.itemDropQuestionDialog = itemDropQuestionDialog

					constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

## 1.) Find this:
	def RequestDropItem(self, answer):
		...
		...

## 2.) Add after this:
	if app.ENABLE_DROP_RENEWAL:
		def RequestDestroyItem(self, answer):
			if not self.itemDropQuestionDialog:
				return
			if answer:
				dropType = self.itemDropQuestionDialog.dropType
				dropNumber = self.itemDropQuestionDialog.dropNumber
				
				if player.SLOT_TYPE_INVENTORY == dropType: ## Ide is kell a speciális leltár izé
				# if player.SLOT_TYPE_INVENTORY == dropType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == dropType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == dropType:
					if dropNumber == player.ITEM_MONEY:
						return
					else:
						self.__SendDestroyItemPacket(dropNumber)

			self.itemDropQuestionDialog.Close()
			self.itemDropQuestionDialog = None
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

		def RequestSellItem(self, answer):
			if not self.itemDropQuestionDialog:
				return
			if answer:
				dropType = self.itemDropQuestionDialog.dropType
				dropNumber = self.itemDropQuestionDialog.dropNumber
				if player.SLOT_TYPE_INVENTORY == dropType: ## és ide is kell!
				# if player.SLOT_TYPE_INVENTORY == dropType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == dropType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == dropType:
					if dropNumber == player.ITEM_MONEY:
						return
					else:
						self.__SendSellItemPacket(dropNumber)

			self.itemDropQuestionDialog.Close()
			self.itemDropQuestionDialog = None
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

## 1.) Find this:
	# PRIVATESHOP_DISABLE_ITEM_DROP
	def __SendDropItemPacket(self, itemVNum, itemCount, itemInvenType = player.INVENTORY):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemDropPacketNew(itemInvenType, itemVNum, itemCount)
	# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP

## 2.) Add after this:
	if app.ENABLE_DROP_RENEWAL:
		def __SendDestroyItemPacket(self, itemVNum, itemInvenType = player.INVENTORY):
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
				return

			net.SendItemDestroyPacket(itemVNum)

		def __SendSellItemPacket(self, itemVNum, itemInvenTyoe = player.INVENTORY):
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
				return

			net.SendItemSellPacket(itemVNum)
