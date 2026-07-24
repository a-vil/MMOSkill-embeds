from . import shot, magic, sblade, martial, halberd


def register_all(bot):
    shot.register(bot)
    magic.register(bot)
    sblade.register(bot)
    martial.register(bot)
    halberd.register(bot)
