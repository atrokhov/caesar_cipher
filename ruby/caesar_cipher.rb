class CesarCipher
  attr_writer :alphabet, :shift

  def initialize(alphabet, shift)
    @alphabet = alphabet
    @shift = shift  
  end

  def encode(plain_text)
    if @alphabet.kind_of?(Array)
      @alphabet = @alphabet.join("")
    end
    
    encoded_text = ''

    plain_text.size.times do |i|
        if @alphabet[plain_text[i]] != nil
            if @alphabet.index(plain_text[i]) + @shift >= @alphabet.size
                shifted_index = @alphabet.index(plain_text[i]) + @shift - @alphabet.size
                while shifted_index >= @alphabet.size
                    shifted_index -= @alphabet.size
                end
                encoded_text += @alphabet[shifted_index]
            else
                encoded_text += @alphabet[@alphabet.index(plain_text[i]) + @shift]
            end
        else
            encoded_text += plain_text[i]
        end
    end
        
    return encoded_text
  end

end 

