step_1:
	@echo "Step 1: Downloading video audio..."
	@make download_video
	@echo "Done."

step_2:
	@echo "Step 2: Splitting audio..."
	@make split_audio
	@echo "Done."

step_3:
	@echo "Step 3: Converting audio to text..."
	@make convert_audio
	@echo "Done."

step_4:
	@echo "Step 4: Merging text files..."
	@make merge_text_files
	@echo "Done."

download_video:
	@python3.12 1_download_video_audio.py

split_audio:
	@python3.12 2_split_audio.py

convert_audio:
	@python3.12 3_convert_audio.py

merge_text_files:
	@python3.12 4_merge_text_files.py

clean:
	@rm -f tmp/*
