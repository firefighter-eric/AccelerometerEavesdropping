package com.hack.accdatarec.util;

import android.content.Context;
import android.media.AudioManager;
import android.media.MediaPlayer;
import android.media.MediaPlayer.OnCompletionListener;
import android.media.MediaPlayer.OnErrorListener;
import android.net.Uri;

import java.io.FileDescriptor;

/**
 * 作者：Rance on 2016/12/15 15:11
 * 邮箱：rance935@163.com
 */
public class MediaManager {

    private static MediaPlayer mMediaPlayer;
    private static boolean isPause;

    /**
     * 播放音乐
     * @param fd
     * @param offset
     * @param length
     */
    public static void playSound(FileDescriptor fd,
                                 long offset,
                                 long length) {
        if (mMediaPlayer == null) {
            mMediaPlayer = new MediaPlayer();

            //设置一个error监听器
            mMediaPlayer.setOnErrorListener(new OnErrorListener() {

                public boolean onError(MediaPlayer arg0, int arg1, int arg2) {
                    mMediaPlayer.reset();
                    return false;
                }
            });
        } else {
            mMediaPlayer.reset();
        }
        try {
            mMediaPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);
            mMediaPlayer.setDataSource(fd, offset, length);
            mMediaPlayer.prepare();
            mMediaPlayer.start();
        } catch (Exception e) {

        }
    }

    /**
     * 暂停播放
     */
    public static void pause() {
        if (mMediaPlayer != null && mMediaPlayer.isPlaying()) { //正在播放的时候
            mMediaPlayer.pause();
            isPause = true;
        }
    }

    /**
     * 当前是isPause状态
     */
    public static void resume() {
        if (mMediaPlayer != null && isPause) {
            mMediaPlayer.start();
            isPause = false;
        }
    }

    /**
     * 释放资源
     */
    public static void release() {
        if (mMediaPlayer != null) {
            mMediaPlayer.release();
            mMediaPlayer = null;
        }
    }
}