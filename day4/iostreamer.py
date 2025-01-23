from io import StringIO

# ... (rest of your code) ...

# Create a StringIO object to capture the streamed output
output_buffer = StringIO()
text_streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True, output_file=output_buffer)

# Generate text, directing output to the StringIO buffer
_ = model.generate(**inputs, streamer=text_streamer, max_new_tokens=1000)

# Get the generated text from the buffer
generated_text = output_buffer.getvalue()

# Print the generated text
print(generated_text)
