// 1.) Find this:
		void		ItemDrop2(LPCHARACTER ch, const char * data);

// 2.) Add after this:
#ifdef ENABLE_DROP_RENEWAL
		void		ItemDestroy(LPCHARACTER ch, const char * data);
		void		ItemSell(LPCHARACTER ch, const char * data);
#endif