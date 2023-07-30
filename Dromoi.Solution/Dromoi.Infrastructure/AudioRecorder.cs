using NAudio.Wave;
using System.Reflection.PortableExecutable;

namespace Dromoi.Infrastructure;
public class AudioRecorder
{

    public void Start()
    {
        var waveIn = new WaveInEvent
        {
            DeviceNumber = 0, // indicates which microphone to use
            WaveFormat = new WaveFormat(rate: 44100, bits: 16, channels: 1),
            BufferMilliseconds = 2000
        };
        waveIn.DataAvailable += WaveIn_DataAvailable;
        waveIn.StartRecording();
    }

    private static void WaveIn_DataAvailable(object? sender, WaveInEventArgs e)
    {
        // copy buffer into an array of integers
        short[] values = new short[e.Buffer.Length / 2];
        Buffer.BlockCopy(e.Buffer, 0, values, 0, e.Buffer.Length);

        // determine the highest value as a fraction of the maximum possible value
        float fraction = (float)values.Max() / 32768;


       
        // print a level meter using the console
        string bar = new('#', (int)(fraction * 70));
        string meter = "[" + bar.PadRight(60, '-') + "]";
        Console.CursorLeft = 0;
        Console.CursorVisible = false;
        var peakFrequency = CalculatePeakFrequency(e);
        ExtractMusicalNote(peakFrequency);
        Console.Write($"{meter} {fraction * 100:00.0}%");
    }

    private static float CalculatePeakFrequency(WaveInEventArgs e)
    {
        var buffer = e.Buffer;
        var bytesRecorded = e.BytesRecorded;

        float max = 0;
        for (int index = 0; index < bytesRecorded - 1; index += 2)
        {
            // Convert bytes to 16-bit PCM sample
            short sample = (short)((buffer[index + 1] << 8) | buffer[index]);

            // Normalize the sample to [-1, 1]
            float sample32 = sample / 32768f;

            // Get the absolute value of the sample
            float absValue = Math.Abs(sample32);

            // Find the maximum value in the buffer
            max = Math.Max(max, absValue);
        }

        // Calculate the peak frequency (frequency with the highest amplitude)
        float peakFrequency = max * 44100; // 44.1 kHz (sample rate)
        return peakFrequency;
    }


    private static void ExtractMusicalNote(float peakFrequency)
    {
        if (peakFrequency <= 1000)
            return;

        // Frequencies of musical notes (A4 = 440 Hz)
        double a4Frequency = 440.0;
        double twelfthRootOf2 = Math.Pow(2.0, 1.0 / 12.0);

        // Calculate the number of half steps away from A4
        double halfStepsFromA4 = 12.0 * Math.Log(peakFrequency / a4Frequency, twelfthRootOf2);

        // Calculate the note index relative to A4 (0 = A4, positive values for higher notes, negative for lower notes)
        int noteIndex = (int)Math.Round(halfStepsFromA4);

        // Array of musical note names
        string[] notes = { "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B" };

        // Calculate the note name and its octave
        int noteNameIndex = (noteIndex + 9) % 12; // "+ 9" to shift the index to start at A
        int octave = 4 + noteIndex / 12;
        
        if(noteNameIndex >=0 )
        {
            string noteName = notes[noteNameIndex];
            Console.Write($"Musical Note: {noteName}{octave}");
            Console.Write($"Peak Frequency: {peakFrequency}");
        }

    }
    // test
    private bool NotePlayed(float[] buffer, int end)
    {
        double power = GoertzelFilter(buffer, TargetFreaquency, buffer.Length);
        if (power > 500) return true;
        return false;
    }

    private double GoertzelFilter(float[] samples, double targetFreaquency, int end)
    {
        double sPrev = 0.0;
        double sPrev2 = 0.0;
        int i;
        double normalizedfreq = targetFreaquency / SampleRate;
        double coeff = 2 * Math.Cos(2 * Math.PI * normalizedfreq);
        for (i = 0; i < end; i++)
        {
            double s = samples[i] + coeff * sPrev - sPrev2;
            sPrev2 = sPrev;
            sPrev = s;
        }
        double power = sPrev2 * sPrev2 + sPrev * sPrev - coeff * sPrev * sPrev2;
        return power;
    }
}