package org.bd.activitydemo

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import io.ktor.client.HttpClient
import io.ktor.client.features.websocket.WebSockets
import io.ktor.client.features.websocket.ws
import io.ktor.http.HttpMethod
import io.ktor.http.cio.websocket.Frame
import io.ktor.http.cio.websocket.readBytes
import io.ktor.http.cio.websocket.readText
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.android.synthetic.main.activity_main.*
import org.kivy.kivynativeactivity.ServiceEcho

class MainActivity : AppCompatActivity() {

    val client = HttpClient {
        install(WebSockets)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun testConnection(ip: String, port: Int, message:String = "Howdii") {
        runBlocking {
            client.ws(
                    method = HttpMethod.Get,
                    host = ip,
                    port = port, path = "/"
            ) {
                send(Frame.Text(message))
                // Receive frame.
                val frame = incoming.receive()
                when (frame) {
                    is Frame.Text -> txtOutput.text=frame.readText()
                    is Frame.Binary -> txtOutput.text=frame.readBytes().toString()
                }
            }
        }
    }

    fun onSend(v: View){

        GlobalScope.launch(Dispatchers.IO) {
            testConnection("localhost", 8081, editMessage.text.toString())
        }
    }

    fun onStart(v: View) {
        val context = applicationContext
        ServiceEcho.prepare(context)
        ServiceEcho.start(context, "")
        btnSend.setEnabled(true)
    }
}
