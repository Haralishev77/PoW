class SHA256:
    def __init__(self):
        self._h = [
            0x6a09e667,
            0xbb67ae85,
            0x3c6ef372,
            0xa54ff53a,
            0x510e527f,
            0x9b05688c,
            0x1f83d9ab,
            0x5be0cd19
        ]
        self.K = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]

    # Функция ROTR
    def _rotr(self, x, n):
        return (x >> n) | (x << (32 - n)) & 0xffffffff

    # Функция SHR
    def _shr(self, x, n):
        return (x >> n) & 0xffffffff

    # Функция Ch
    def _ch(self, x, y, z):
        return (x & y) ^ (~x & z)

    # Функция Maj
    def _maj(self, x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)

    # Функция Sigma0
    def _sigma_big_0(self, x):
        return self._rotr(x, 2) ^ self._rotr(x, 13) ^ self._rotr(x, 22)

    # Функция Sigma1
    def _sigma_big_1(self, x):
        return self._rotr(x, 6) ^ self._rotr(x, 11) ^ self._rotr(x, 25)

    # Функция sigma0
    def _sigma_small_0(self, x):
        return self._rotr(x, 7) ^ self._rotr(x, 18) ^ self._shr(x, 3)

    # Функция sigma1
    def _sigma_small_1(self, x):
        return self._rotr(x, 17) ^ self._rotr(x, 19) ^ self._shr(x, 10)

    # Функция хеширования блока
    def _sha256_block(self, chunk):
        # Шаг 1
        w = [0] * 64
        for i in range(16):
            w[i] = int.from_bytes(chunk[i * 4:(i + 1) * 4], byteorder='big')

        for i in range(16, 64):
            w[i] = (self._sigma_small_1(w[i - 2]) + w[i - 7] + self._sigma_small_0(w[i - 15]) + w[i - 16]) & 0xffffffff

        # Шаг 2
        a, b, c, d, e, f, g, h = self._h

        # Шаг 3
        for i in range(64):
            t1 = (h + self._sigma_big_1(e) + self._ch(e, f, g) + self.K[i] + w[i]) & 0xffffffff
            t2 = (self._sigma_big_0(a) + self._maj(a, b, c)) & 0xffffffff
            h = g
            g = f
            f = e
            e = (d + t1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xffffffff

        # Шаг 4
        self._h = [(x + y) & 0xffffffff for x, y in zip(self._h, [a, b, c, d, e, f, g, h])]

    # Функция обновления
    def update(self, data):
        buffer = bytearray(data)
        padding_length = (55 - len(data) % 64) if (len(data) % 64) < 56 else (119 - len(data) % 64)
        padding = b'\x80' + b'\x00' * padding_length + (len(data) * 8).to_bytes(8, byteorder='big')
        buffer.extend(padding)

        while len(buffer) >= 64:
            self._sha256_block(buffer[:64])
            del buffer[:64]

    # Функция возврата хэша
    def digest(self, data=None):
        if data:
            self.reset()
            self.update(data)
        return b''.join(h.to_bytes(4, byteorder='big') for h in self._h)

    # Функция возврата хэша в шестнадцатеричной системе счисления
    def hexdigest(self, data=None):
        return self.digest(data).hex()

    # Функция сброса значений
    def reset(self):
        self.__init__()
