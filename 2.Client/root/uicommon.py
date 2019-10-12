## 1.) Go to the end line and add the new line:
if app.ENABLE_DROP_RENEWAL:
	class DropRenewalDialog(ui.ScriptWindow):
		def __init__(self):
			ui.ScriptWindow.__init__(self)
			self.__CreateDialog()

		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def __CreateDialog(self):
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/DropRenewal/DropRenewalDialog.py")
			self.board			= self.GetChild("DropRenewalBoard")
			self.textLine		= self.GetChild("MessageBox")
			self.textLineTwo	= self.GetChild("MessageBoxTwo")
			self.textLineThree	= self.GetChild("MessageBoxThree")
			self.acceptButton	= self.GetChild("DropButton")
			self.destroyButton	= self.GetChild("DestroyButton")
			self.sellButton		= self.GetChild("SellButon")
			self.cancelButton	= self.GetChild("CancelButton")
			self.itemSlot		= self.GetChild("ItemSlot")
			try:
				self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
				self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			except:
				dbg.TraceError("")

		def SetItemSlot(self, slotIndex):
			itemIndex	= player.GetItemIndex(slotIndex)
			itemCount	= player.GetItemCount(slotIndex)
			itemSell	= localeInfo.NumberToMoneyString(player.GetISellItemPrice(slotIndex))
			self.itemSlot.SetItemSlot(0, itemIndex, itemCount)

			item.SelectItem(player.GetItemIndex(slotIndex))

			metinSlot	= [player.GetItemMetinSocket(slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			attrSlot	= [player.GetItemAttribute(slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
			
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_DROP):
				self.acceptButton.Down()
				self.acceptButton.Disable()
			
			self.itemToolTip = uiToolTip.ItemToolTip()
			self.itemToolTip.AddItemData(player.GetItemIndex(slotIndex), metinSlot, attrSlot)
			
			if itemCount <= 1:
				self.SetText(localeInfo.DROP_RENEWAL_ITEM_NAME % (item.GetItemName()))
				self.SetTextTwo(localeInfo.DROP_RENEWAL_SALES % (str(itemSell)))
			else:
				self.SetText(localeInfo.DROP_RENEWAL_ITEM_COUNT % (item.GetItemName(),str(itemCount)))
				self.SetTextTwo(localeInfo.DROP_RENEWAL_SALES % (str(itemSell)))

		def Open(self):
			if 0 != self.itemToolTip:
				self.itemToolTip.HideToolTip()
				
			self.SetCenterPosition()
			self.SetTop()
			self.Show()

		def Close(self):
			if 0 != self.itemToolTip:
				self.itemToolTip.HideToolTip()
			self.Hide()

		def SetWidth(self, width):
			height = self.GetHeight()
			self.SetSize(width, height)
			self.board.SetSize(width, height)
			self.SetCenterPosition()
			self.UpdateRect()

		def OverInItem(self, slotNumber):
			if 0 != self.itemToolTip:
				self.itemToolTip.ShowToolTip()
				
		def OverOutItem(self):
			if 0 != self.itemToolTip:
				self.itemToolTip.HideToolTip()

		def SAFE_SetAcceptEvent(self, event):
			self.acceptButton.SAFE_SetEvent(event)

		def SAFE_SetCancelEvent(self, event):
			self.cancelButton.SAFE_SetEvent(event)

		def SetAcceptEvent(self, event):
			self.acceptButton.SetEvent(event)

		def SetDestroyEvent(self, event):
			self.destroyButton.SetEvent(event)

		def SetSellEvent(self, event):
			self.sellButton.SetEvent(event)

		def SetCancelEvent(self, event):
			self.cancelButton.SetEvent(event)

		def SetText(self, text):
			self.textLine.SetText(text)
			# self.textLine.SetFontColor(0.72, 1.0, 0.0)

		def SetTextTwo(self, text):
			self.textLineTwo.SetText(text)
			# self.textLineTwo.SetFontColor(0.72, 1.0, 0.0)

		def SetTextThree(self, text):
			self.textLineThree.SetText(text)
			# self.textLineThree.SetFontColor(0.72, 1.0, 0.0)

		def SetAcceptText(self, text):
			self.acceptButton.SetText(text)

		def SetCancelText(self, text):
			self.cancelButton.SetText(text)

		def OnPressEscapeKey(self):
			self.Close()
			return True
