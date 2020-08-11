import logging

import package

logger = logging.getLogger(__name__)

package.add_file_handler(logger=logger, level=logging.DEBUG, tag="debug")
package.add_file_handler(logger=logger, level=logging.ERROR, tag="error")
