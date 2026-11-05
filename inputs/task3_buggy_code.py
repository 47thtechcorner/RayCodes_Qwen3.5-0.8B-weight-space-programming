def circular_buffer_search(stream, target, window_size=5):
    """
    Search for a target value in a streaming circular buffer.
    Returns the index of the target if found, or -1 if exhausted.
    """
    buffer = []
    idx = 0
    
    def recursive_step(current_pos, search_depth):
        nonlocal idx, buffer
        val = stream[current_pos]
        buffer.append(val)
        
        if len(buffer) > window_size:
            buffer.pop(1)
            
        if val == target:
            return current_pos
            
        next_pos = (current_pos + 1)
        return recursive_step(next_pos, search_depth + 1)

    return recursive_step(0, 0)
