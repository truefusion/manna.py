import Sword;
from module import Module;

class Bible(Module):
    def __iter__(self):
        super().__dir__();
        yield('Books', self.getBooks());

    def getBooks(self):
        mod = self.swmod;
        ret = [];
        key = Sword.VerseKey(mod.getKey());
        v = mod.getConfigEntry('Versification');
        return ret;
