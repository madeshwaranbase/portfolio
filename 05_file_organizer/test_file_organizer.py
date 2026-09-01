"""
Unit tests for file_organizer.py
Run: pytest test_file_organizer.py -v
"""
import pytest
from file_organizer import classify_file, organize_folder, OTHERS_CATEGORY


class TestClassifyFile:
    def test_image_extension(self):
        assert classify_file("photo.JPG") == "Images"

    def test_document_extension(self):
        assert classify_file("report.pdf") == "Documents"

    def test_video_extension(self):
        assert classify_file("clip.mp4") == "Videos"

    def test_music_extension(self):
        assert classify_file("song.mp3") == "Music"

    def test_unknown_extension_goes_to_others(self):
        assert classify_file("archive.zip") == OTHERS_CATEGORY

    def test_no_extension_goes_to_others(self):
        assert classify_file("README") == OTHERS_CATEGORY

    def test_case_insensitive(self):
        assert classify_file("IMAGE.PNG") == "Images"


class TestOrganizeFolder:
    def test_missing_folder_raises(self, tmp_path):
        missing = tmp_path / "does_not_exist"
        with pytest.raises(FileNotFoundError):
            organize_folder(missing)

    def test_moves_files_into_category_folders(self, tmp_path):
        (tmp_path / "photo.jpg").write_text("fake image data")
        (tmp_path / "report.pdf").write_text("fake pdf data")

        log = organize_folder(tmp_path)

        assert (tmp_path / "Images" / "photo.jpg").exists()
        assert (tmp_path / "Documents" / "report.pdf").exists()
        assert not (tmp_path / "photo.jpg").exists()
        assert len(log) == 2

    def test_unrecognized_extension_goes_to_others_folder(self, tmp_path):
        (tmp_path / "data.zip").write_text("fake zip data")
        organize_folder(tmp_path)
        assert (tmp_path / OTHERS_CATEGORY / "data.zip").exists()

    def test_skips_existing_file_at_destination(self, tmp_path):
        (tmp_path / "Images").mkdir()
        (tmp_path / "Images" / "photo.jpg").write_text("already here")
        (tmp_path / "photo.jpg").write_text("new file")

        log = organize_folder(tmp_path)

        assert "Skipped existing file: photo.jpg" in log[0]
        assert (tmp_path / "photo.jpg").exists()  # not moved

    def test_ignores_subdirectories(self, tmp_path):
        (tmp_path / "subfolder").mkdir()
        log = organize_folder(tmp_path)
        assert log == []

    def test_empty_folder_produces_no_log(self, tmp_path):
        assert organize_folder(tmp_path) == []
