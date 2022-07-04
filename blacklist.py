
def get_blacklist(platform):
    if platform == 'Game Boy':
        return ['COMMODORE', 'GAME BOY COLOR', 'GAMEBOY COLOR', '(GBC)', 'GBC', 'GBA', '(GBA)', 'GAMEBOY ADVANCE', 'GAME BOY ADVANCE', 'MEGADRIVE', 'MEGA DRIVE', 'GENESIS', 'XBOX', 'XBOX360', 'XBOX1', 'XB', 'XB1', 'PLAYSTATION', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5', 'GAME GEAR', 'MASTER SYSTEM', 'NES', 'SNES', 'WII', 'GAME CUBE', 'NINTENDO 64', 'N64', 'NINTENDO64', 'NINTENDO SWITCH', 'PSP', 'PSVITA', 'SEGA', 'SONY', 'MICROSOFT', 'DREAMCAST', 'CD', 'DVD', 'VHS', 'Paquete De Juegos', 'lote', 'lot', 'bundle', 'muñeco', 'figura', 'reloj', 'imán', 'iman', 'magnet', 'sudadera', 'camisa', 'camiseta']
    if platform == 'Game Boy Color':
        return ['PS1', 'COMMODORE', 'DMG', '(GB)', 'GB', 'GBA', '(GBA)', 'GAMEBOY ADVANCE', 'GAME BOY ADVANCE', 'MEGADRIVE', 'MEGA DRIVE', 'GENESIS', 'XBOX', 'XBOX360', 'XBOX1', 'XB', 'XB1', 'PLAYSTATION', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5', 'GAME GEAR', 'MASTER SYSTEM', 'NES', 'SNES', 'WII', 'GAME CUBE', 'NINTENDO 64', 'N64', 'NINTENDO64', 'NINTENDO SWITCH', 'PSP', 'PSVITA', 'SEGA', 'SONY', 'MICROSOFT', 'DREAMCAST', 'CD', 'DVD', 'VHS', 'Paquete De Juegos', 'lote', 'lot', 'bundle', 'muñeco', 'figura', 'reloj', 'imán', 'iman', 'magnet', 'sudadera', 'camisa', 'camiseta']
    if platform == 'SEGA MegaDrive':
        return ['COMMODORE', 'GAME BOY COLOR', 'GAMEBOY COLOR', '(GBC)', 'DMG', '(GB)', 'GB', 'GBA', '(GBA)', 'GAMEBOY ADVANCE', 'GAME BOY ADVANCE', 'XBOX', 'XBOX360', 'XBOX1', 'XB', 'XB1', 'PLAYSTATION', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5', 'GAME GEAR', 'MASTER SYSTEM', 'NES', 'SNES', 'WII', 'GAME CUBE', 'NINTENDO 64', 'N64', 'NINTENDO64', 'NINTENDO SWITCH', 'PSP', 'PSVITA', 'SEGA', 'SONY', 'MICROSOFT', 'DREAMCAST', 'CD', 'DVD', 'VHS', 'Paquete De Juegos', 'lote', 'lot', 'bundle', 'muñeco', 'figura', 'reloj', 'imán', 'iman', 'magnet', 'sudadera', 'camisa', 'camiseta']
    if platform == 'NES':
        return ['MEGADRIVE', 'MEGA DRIVE', 'GENESIS', 'COMMODORE', 'GAME BOY COLOR', 'GAMEBOY COLOR', '(GBC)', 'DMG', '(GB)', 'GB', 'GBA', '(GBA)', 'GAMEBOY ADVANCE', 'GAME BOY ADVANCE', 'XBOX', 'XBOX360', 'XBOX1', 'XB', 'XB1', 'PLAYSTATION', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5', 'GAME GEAR', 'MASTER SYSTEM', 'SNES', 'WII', 'GAME CUBE', 'NINTENDO 64', 'N64', 'NINTENDO64', 'NINTENDO SWITCH', 'PSP', 'PSVITA', 'SEGA', 'SONY', 'MICROSOFT', 'DREAMCAST', 'CD', 'DVD', 'VHS', 'Paquete De Juegos', 'lote', 'lot', 'bundle', 'muñeco', 'figura', 'reloj', 'imán', 'iman', 'magnet', 'sudadera', 'camisa', 'camiseta']
    if platform == 'SNES':
        return ['MEGADRIVE', 'MEGA DRIVE', 'GENESIS', 'COMMODORE', 'GAME BOY COLOR', 'GAMEBOY COLOR', '(GBC)', 'DMG', '(GB)', 'GB', 'GBA', '(GBA)', 'GAMEBOY ADVANCE', 'GAME BOY ADVANCE', 'XBOX', 'XBOX360', 'XBOX1', 'XB', 'XB1', 'PLAYSTATION', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5', 'GAME GEAR', 'MASTER SYSTEM', 'NES', 'WII', 'GAME CUBE', 'NINTENDO 64', 'N64', 'NINTENDO64', 'NINTENDO SWITCH', 'PSP', 'PSVITA', 'SEGA', 'SONY', 'MICROSOFT', 'DREAMCAST', 'CD', 'DVD', 'VHS', 'Paquete De Juegos', 'lote', 'lot', 'bundle', 'muñeco', 'figura', 'reloj', 'imán', 'iman', 'magnet', 'sudadera', 'camisa', 'camiseta']
    if platform == 'Playstation 1':
        return ['MEGADRIVE', 'MEGA DRIVE', 'GENESIS', 'COMMODORE', 'GAME BOY COLOR', 'GAMEBOY COLOR', '(GBC)', 'DMG', '(GB)', 'GB', 'GBA', '(GBA)', 'GAMEBOY ADVANCE', 'GAME BOY ADVANCE', 'XBOX', 'XBOX360', 'XBOX1', 'XB', 'XB1', 'PLAYSTATION', 'PS2', 'PS3', 'PS4', 'PS5', 'GAME GEAR', 'MASTER SYSTEM', 'NES', 'SNES', 'WII', 'GAME CUBE', 'NINTENDO 64', 'N64', 'NINTENDO64', 'NINTENDO SWITCH', 'PSP', 'PSVITA', 'SEGA', 'MICROSOFT', 'DREAMCAST', 'CD', 'DVD', 'VHS', 'Paquete De Juegos', 'lote', 'lot', 'bundle', 'muñeco', 'figura', 'reloj', 'imán', 'iman', 'magnet', 'sudadera', 'camisa', 'camiseta']
    if platform == 'Playstation 2':
        return ['MEGADRIVE', 'MEGA DRIVE', 'GENESIS', 'COMMODORE', 'GAME BOY COLOR', 'GAMEBOY COLOR', '(GBC)', 'DMG', '(GB)', 'GB', 'GBA', '(GBA)', 'GAMEBOY ADVANCE', 'GAME BOY ADVANCE', 'XBOX', 'XBOX360', 'XBOX1', 'XB', 'XB1', 'PLAYSTATION', 'PS1', 'PS3', 'PS4', 'PS5', 'GAME GEAR', 'MASTER SYSTEM', 'NES', 'SNES', 'WII', 'GAME CUBE', 'NINTENDO 64', 'N64', 'NINTENDO64', 'NINTENDO SWITCH', 'PSP', 'PSVITA', 'SEGA', 'MICROSOFT', 'DREAMCAST', 'CD', 'DVD', 'VHS', 'Paquete De Juegos', 'lote', 'lot', 'bundle', 'muñeco', 'figura', 'reloj', 'imán', 'iman', 'magnet', 'sudadera', 'camisa', 'camiseta']
    if platform == 'SEGA Dreamcast':
        return ['MEGADRIVE', 'MEGA DRIVE', 'GENESIS', 'COMMODORE', 'GAME BOY COLOR', 'GAMEBOY COLOR', '(GBC)', 'DMG', '(GB)', 'GB', 'GBA', '(GBA)', 'GAMEBOY ADVANCE', 'GAME BOY ADVANCE', 'XBOX', 'XBOX360', 'XBOX1', 'XB', 'XB1', 'PLAYSTATION', 'PS1', 'PS3', 'PS4', 'PS5', 'GAME GEAR', 'MASTER SYSTEM', 'NES', 'SNES', 'WII', 'GAME CUBE', 'NINTENDO 64', 'N64', 'NINTENDO64', 'NINTENDO SWITCH', 'PSP', 'PSVITA', 'SONY', 'MICROSOFT', 'CD', 'DVD', 'VHS', 'Paquete De Juegos', 'lote', 'lot', 'bundle', 'muñeco', 'figura', 'reloj', 'imán', 'iman', 'magnet', 'sudadera', 'camisa', 'camiseta']
    else:
        return ['MEGADRIVE', 'MEGA DRIVE', 'GENESIS', 'COMMODORE', 'GAME BOY COLOR', 'GAMEBOY COLOR', '(GBC)', 'DMG', '(GB)', 'GB', 'GBA', '(GBA)', 'GAMEBOY ADVANCE', 'GAME BOY ADVANCE', 'XBOX', 'XBOX360', 'XBOX1', 'XB', 'XB1', 'PLAYSTATION', 'PS1', 'PS3', 'PS4', 'PS5', 'GAME GEAR', 'MASTER SYSTEM', 'NES', 'SNES', 'WII', 'GAME CUBE', 'NINTENDO 64', 'N64', 'NINTENDO64', 'NINTENDO SWITCH', 'PSP', 'PSVITA', 'SONY', 'MICROSOFT', 'SEGA', 'DREAMCAST', 'CD', 'DVD', 'VHS', 'Paquete De Juegos', 'lote', 'lot', 'bundle', 'muñeco', 'figura', 'reloj', 'imán', 'iman', 'magnet', 'sudadera', 'camisa', 'camiseta']
