# Part 1 goes here!
# create two exception class
class DecodeError(Exception):
    pass

class ChunkError(Exception):
    pass

class BitList:
    bitstring = ''

    def __init__(self, binary_str):
        p = set(binary_str)
        s = {'0', '1'}
        if not (s==p or p == {'0'} or p =={'1'}):
            raise ValueError('Format is invalid; does not consist of only 0 and 1')
        self.bitstring = binary_str


        
    def __str__(self):
        return self.bitstring

    def __eq__(self, other):
        return self.bitstring == other.bitstring
    
    def arithmetic_shift_left(self):
        self.bitstring = self.bitstring[1:]+'0'
    
    def arithmetic_shift_right(self):
        self.bitstring = self.bitstring[0] + self.bitstring[:-1]
    
    def bitwise_and(self, other):
        self_bitstring = self.bitstring
        other_bitstring = other.bitstring
        try:
            b_and = ''
            for i in range(len(self_bitstring)):
                b_and += str(int(self_bitstring[i]) * int(other_bitstring[i]))
            return BitList(b_and)
        except:
            print('length not equal')


    def chunk(self, chunk_length):
        bit_string = self.bitstring
        if len(bit_string)%chunk_length ==0:
            bitlist = []
            for i in range(0, len(bit_string), chunk_length):
                add_chunk = list(bit_string[i:i+chunk_length])
                add_chunk = [int(i) for i in add_chunk]
                bitlist.append(add_chunk)
            return bitlist
        else:
            raise ChunkError()


    def decode(self, encoding='utf-8'):
        if encoding not in ('utf-8', 'us-ascii'):
            raise ValueError('The encoding is not supported.')
        bit_string = self.bitstring
        #print(f'what is bit_string{bit_string}')
        if encoding == 'utf-8':
            if len(bit_string)==8 and bit_string[0]!='0':
                raise DecodeError()

            chunk_list = []
            for i in range(0, len(bit_string), 8):
                chunk_list.append(bit_string[i:i+8])
            #print(f'what is chunk_list:{chunk_list}')

            more_chunk = []
            j = 0
            while j < len(chunk_list):
                chunk = chunk_list[j]
                leading1 = chunk.find('0')
                if leading1>1:
                    small_chunk = chunk_list[j:j+leading1]
                    j += leading1
                elif leading1 ==0:
                    small_chunk = [chunk_list[j]]
                    j +=1
                more_chunk.append(small_chunk)
              
            #print(f'what is more_chunk:{more_chunk}')

            try:
                decoded_string = ''
                for small_chunk in more_chunk:
                    b = bytes(int(i, 2) for i in small_chunk)
                    decoded_character = b.decode(encoding)
                    decoded_string +=decoded_character
            except:
                raise DecodeError  
        else:
            chunk_list = []
            if len(bit_string)%7 !=0:
                raise DecodeError
            else:
                for i in range(0, len(bit_string), 7):
                    chunk_list.append(bit_string[i:i+7])
                try:
                    b = bytes(int(i, 2) for i in chunk_list)
                    decoded_string = b.decode(encoding) 
                except:
                    raise DecodeError  
        return decoded_string


    
    @staticmethod
    def from_ints(*args):
        bitstring = ''
        for arg in args:
            bitstring += str(arg)
        p = set(bitstring)
        s = {'0', '1'}
        if not (s==p or p == {'0'} or p =={'1'}):
            raise ValueError('Format is invalid; does not consist of only 0 and 1')
        return BitList(bitstring)





