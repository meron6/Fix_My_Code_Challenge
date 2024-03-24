result = []
ARGV.each do |arg|
    # skip if not integer
    next if arg !~ /^-?[0-9]+$/

    # convert to integer
    i_arg = arg.to_i
    
    # if result is empty or the last element is less than the current integer,
    # append it to the end
    if result.empty? || result.last < i_arg
        result << i_arg
    else
        # find the correct position to insert the integer
        i = 0
        while i < result.size && result[i] < i_arg
            i += 1
        end
        # insert the integer at the correct position
        result.insert(i, i_arg)
    end
end

puts result
