invite_list = ['Jall', 'Artin', 'Mehdi', 'Baran', 'Parmis']
print(f"I have invited {len(invite_list)} people for dinner at first.")
invite_list.append('Amin')
invite_list.insert(0, 'Mohammad')
invite_list.insert(4, 'Mahtaa')
print(f"I have invited {len(invite_list)} people for dinner after finding bigger table.")
del invite_list[0]
del invite_list[1]
del invite_list[1]
del invite_list[1]
del invite_list[1]
del invite_list[2]
print(f"I have invited {len(invite_list)} people for dinner at end.")