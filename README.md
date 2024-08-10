<h1>Numerix</h1>

<p>Numerix is a GenAI-based agent designed to solve mathematical problems using the latest advancements in AI. It leverages multiple tools and a powerful language model to provide accurate and efficient solutions to complex mathematical queries.</p>

<h2>Tools Used</h2>
<ul>
    <li><strong>Langchain</strong>: For managing the interaction between the agent and various tools.</li>
    <li><strong>Groq</strong>: To enhance computational efficiency.</li>
    <li><strong>Streamlit</strong>: For the user interface.</li>
    <li><strong>Wikipedia</strong>: Used as a knowledge base for retrieving relevant information.</li>
</ul>

<h2>Model Used</h2>
<ul>
    <li><strong>Gemma2-9b-It</strong>: A large language model utilized by Numerix to understand and solve mathematical problems.</li>
</ul>

<h2>Agent Capabilities</h2>

<p>Numerix employs the following tools to solve mathematical problems:</p>
<ol>
    <li><strong>Wikipedia Tool</strong>: Retrieves relevant information from Wikipedia.</li>
    <li><strong>LLMMathChain (Calculator Tool)</strong>: Handles calculations and mathematical operations.</li>
    <li><strong>ReAct (Reasoning Tool)</strong>: Provides reasoning and logical deductions for problem-solving.</li>
</ol>

<h2>How It Works</h2>

<p>Numerix takes a mathematical question as input and processes it using the three tools mentioned above. The agent then returns the answer to the query. <strong>Note:</strong> The question should be asked in an understandable manner for the best results.</p>

<h2>Setup Instructions</h2>
<ol>
    <li><strong>Clone the Repository</strong>: Clone the Numerix repository to your local machine.
        <pre><code>git clone https://github.com/ayuk007/Numerix.git</code></pre>
    </li>
    <li><strong>Install Dependencies</strong>: Navigate to the project directory and install the necessary dependencies.
        <pre><code>cd Numerix
pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Set Up Environment Variables</strong>: Create a <code>.env</code> file in the root directory of the project and include your Langchain and Groq API keys.
        <pre><code>LANGCHAIN_API_KEY=your_langchain_api_key
GROQ_API_KEY=your_groq_api_key</code></pre>
    </li>
    <li><strong>Run the Application</strong>: Use Streamlit to run the Numerix application.
        <pre><code>streamlit run app.py</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Open the Numerix application in your web browser.</li>
    <li>Enter a mathematical question in the input field.</li>
    <li>Click the "Answer" button to get the answer.</li>
</ol>

<h2>Contributing</h2>

<p>We welcome contributions to enhance Numerix! Please fork the repository, make your changes, and submit a pull request.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License. See the LICENSE file for details.</p>

<h2>Acknowledgments</h2>

<p>Special thanks to the developers and communities behind Langchain, Groq, Streamlit, and Wikipedia for their invaluable tools and resources.</p>
