from . import shot, magic, sblade, martial, halberd, assassin


def register_all(bot):
    shot.register(bot)
    magic.register(bot)
    sblade.register(bot)
    martial.register(bot)
    halberd.register(bot)
    assassin.register(bot)
